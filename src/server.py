from mcp.server.fastmcp import FastMCP
from src.tools.leads import search_leads_serp, research_company_tavily
from src.tools.crm import add_to_hubspot
from src.tools.email import draft_outreach

mcp = FastMCP("Sales-Automation")

@mcp.tool()
async def find_and_research_lead(company_name: str, person_name: str):
    """
    Complete workflow: Researches a company via Tavily and finds contact info via SerpApi.
    """
    research = await research_company_tavily(company_name)
    leads = await search_leads_serp(f"{person_name} at {company_name}")
    
    return {
        "company_insights": research[:2],
        "contact_links": leads
    }

@mcp.tool()
async def sync_lead_and_email(name: str, email: str, company: str, insights: str):
    """Syncs lead to CRM and returns a personalized email draft."""
    crm_status = await add_to_hubspot(name, email, company)
    email_draft = await draft_outreach(name, insights)
    
    return f"{crm_status}\n\nDraft:\n{email_draft}"

if __name__ == "__main__":
    mcp.run()