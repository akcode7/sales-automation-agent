# Multi-stage build for minimal final image
FROM python:3.12-alpine AS python-builder

# Install Python build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev

# Copy uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
RUN chmod +x /usr/local/bin/uv

# Create virtual environment and install Python MCP dependencies
RUN uv venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and wheel to fix CVEs
RUN uv pip install --upgrade wheel>=0.46.2 pip>=25.3

# Copy requirements and install dependencies
WORKDIR /build
COPY requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt

# Final stage - minimal runtime image with Python 3.12
FROM python:3.12-alpine

# Install runtime dependencies
RUN apk add --no-cache \
    libstdc++ \
    libgcc \
    openssl \
    ca-certificates \
    libffi \
    tini && \
    # Upgrade OpenSSL to patch CVEs
    apk upgrade --no-cache openssl

# Upgrade system pip to fix CVEs
RUN pip install --upgrade pip>=25.3

# Copy Python environment from builder
COPY --from=python-builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Update CA certificates
RUN update-ca-certificates

# Create non-root user for running MCP server
RUN addgroup -g 1000 mcp && \
    adduser -u 1000 -G mcp -D -h /home/mcp mcp

# Set up working directory
WORKDIR /home/mcp/app

# Copy application source code
COPY --chown=mcp:mcp src/ ./src/

# Switch to non-root user
USER mcp

# Common environment variables for MCP servers
ENV MCP_ENV=production

# Health check for container monitoring
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python3 -c "import sys; sys.exit(0)"

# Use tini for proper signal handling
ENTRYPOINT ["/sbin/tini", "--"]

# Run the MCP server
CMD ["python", "-m", "src.server"]
