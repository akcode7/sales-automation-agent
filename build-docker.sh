#!/bin/bash
# Build script for Sales Automation MCP Docker image
# Uses Python 3.12 Alpine with security patches and multi-stage build

IMAGE_NAME="sales-automation-mcp"
VERSION="latest"

echo "🐳 Building secure Docker image: ${IMAGE_NAME}:${VERSION}"
echo "   - Multi-stage build for minimal size"
echo "   - Python 3.12 Alpine base"
echo "   - Security patches applied"
echo "   - Non-root user execution"
echo ""

# Build the image
docker build -t ${IMAGE_NAME}:${VERSION} .

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Docker image built successfully!"
    echo ""
    echo "📋 Image details:"
    docker images ${IMAGE_NAME}:${VERSION}
    echo ""
    echo "🚀 To test locally on Ubuntu:"
    echo "   docker run --env-file .env ${IMAGE_NAME}:${VERSION}"
    echo ""
    echo "   Or pass individual environment variables:"
    echo "   docker run -e GOOGLE_MAPS_API_KEY=xxx \\"
    echo "              -e TAVILY_API_KEY=xxx \\"
    echo "              -e CRM_API_KEY=xxx \\"
    echo "              -e EMAIL_API_KEY=xxx \\"
    echo "              -e VERIFIED_TEST_EMAIL=xxx \\"
    echo "              ${IMAGE_NAME}:${VERSION}"
    echo ""
    echo "🔍 To verify the image:"
    echo "   docker run --rm ${IMAGE_NAME}:${VERSION} python3 --version"
    echo ""
    echo "📦 To tag and use in Archestra:"
    echo "   docker tag ${IMAGE_NAME}:${VERSION} ${IMAGE_NAME}:$(date +%Y%m%d)"
    echo "   # Then use '${IMAGE_NAME}:latest' in Archestra UI"
    echo ""
    echo "🔐 Image built with security features:"
    echo "   ✓ Non-root user (uid=1000, gid=1000)"
    echo "   ✓ CVE patches applied"
    echo "   ✓ Minimal attack surface (Alpine-based)"
    echo "   ✓ Health checks enabled"
else
    echo ""
    echo "❌ Docker build failed!"
    exit 1
fi
