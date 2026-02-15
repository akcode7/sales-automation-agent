# Sales Automation MCP
Built for [Archestra.ai](https://archestra.ai)

## Configuration in Archestra
1. Build & Push: `docker build -t your-repo/sales-mcp:latest . && docker push your-repo/sales-mcp:latest`
2. Add to Archestra Private Registry: Use the image tag above.
3. Add Secrets:
   - `SERPAPI_API_KEY`
   - `TAVILY_API_KEY`
   - `CRM_API_KEY` -> (hubspot)
   - `EMAIL_API_KEY` -> (Resend)