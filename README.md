# Sales Automation MCP
Built for [Archestra.ai](https://archestra.ai)

## Configuration in Archestra
1. Build & Push: `docker build -t your-repo/sales-mcp:latest . && docker push your-repo/sales-mcp:latest`
2. Add to Archestra Private Registry: Use the image tag above.
3. Add Secrets:
   - `GOOGLE_MAPS_API_KEY`
   - `TAVILY_API_KEY`
   - `CRM_API_KEY` -> (hubspot)
   - `EMAIL_API_KEY` -> (Resend)

 # Sales Automation Agent

An AI-powered sales prospecting agent built for [Archestra.ai](https://archestra.ai) that automates the entire lead generation workflow from Google Maps discovery to HubSpot CRM integration.

## What It Does

This MCP server enables AI agents to execute a complete sales prospecting workflow:

1. **Find Local Businesses** - Search Google Maps for businesses by industry and location
   - Target specific industries (restaurants, gyms, law firms, etc.)
   - Filter by geographic area
   - Get business details (name, address, phone, website, rating)

2. **Research Companies** - Automatically gather sales intelligence using Tavily AI
   - Company background and recent news
   - Decision maker information
   - Industry trends and pain points
   - Conversation starters for outreach

3. **Sync to HubSpot CRM** - Push qualified leads with enriched data
   - Create/update contacts automatically
   - Add detailed research notes
   - Track lead source and lifecycle stage
   - Include relevant tags and properties

## Use Cases

- **Outbound Sales Teams** - Build targeted prospect lists by geography and vertical
- **Sales Development Reps** - Automate research before cold outreach
- **Account-Based Marketing** - Identify and qualify accounts in specific regions
- **Lead Enrichment** - Keep CRM updated with fresh intelligence

## Tools Available

### `find_businesses_on_maps`
Search Google Maps for potential customers by industry and location.

**Parameters:**
- `query` (string) - Search term (e.g., "restaurants in San Francisco")
- `location` (string, optional) - Geographic area to search

**Returns:** List of businesses with contact info, ratings, and address

### `research_company_tavily`
Deep research on a company using AI-powered web search.

**Parameters:**
- `company_name` (string) - Name of the company to research
- `company_website` (string, optional) - Company website URL

**Returns:** Comprehensive company intelligence including background, decision makers, and insights

### `sync_to_hubspot`
Create or update a contact in HubSpot CRM.

**Parameters:**
- `email` (string) - Contact email
- `first_name` (string) - First name
- `last_name` (string) - Last name
- `company` (string, optional) - Company name
- `phone` (string, optional) - Phone number
- `website` (string, optional) - Website URL
- `notes` (string, optional) - Research notes or context

**Returns:** Confirmation with HubSpot contact ID

## Setup & Deployment

### 1. Build Docker Image

```bash
docker build -t your-registry/sales-automation-mcp:latest .
docker push your-registry/sales-automation-mcp:latest