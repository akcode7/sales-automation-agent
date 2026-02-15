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

   # Sales Automation MCP

An AI-powered sales prospecting agent that automates lead generation from Google Maps to HubSpot CRM.

## What It Does

This MCP server enables AI agents to:

1. **Find Leads** - Search Google Maps for businesses by industry and location (e.g., "restaurants in San Francisco")
2. **Research Companies** - Automatically gather intelligence on each lead using Tavily AI search:
   - Company background and recent news
   - Decision maker information
   - Industry insights and pain points
3. **Sync to CRM** - Push qualified leads directly to HubSpot with enriched data and notes

## Perfect For

- Sales teams doing outbound prospecting
- Building targeted lead lists by geography and industry
- Automating the research phase of sales development
- Keeping your CRM updated with qualified, contextualized leads

## Tools Included

- `find_businesses_on_maps` - Search Google Maps for potential customers
- `research_company_tavily` - Deep research on companies and decision makers
- `sync_to_hubspot` - Create/update contacts in HubSpot CRM

## Configuration in Archestra

1. Build & Push: `docker build -t your-repo/sales-mcp:latest . && docker push your-repo/sales-mcp:latest`
2. Add to Archestra Private Registry: Use the image tag above.