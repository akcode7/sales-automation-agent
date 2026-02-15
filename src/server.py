from mcp.server.fastmcp import FastMCP
from src.tools.maps import find_businesses_on_maps
from src.tools.leads import research_company_tavily
from src.tools.crm import sync_to_hubspot
from src.tools.email import send_sales_outreach

mcp = FastMCP("Sales-Lead-Gen")

@mcp.tool()
async def search_and_research(industry: str, city: str):
    """Finds companies on Google Maps and immediately researches them with Tavily."""
    raw_leads = await find_businesses_on_maps(industry, city)
    enriched_leads = []
    
    for lead in raw_leads:
        # Research each lead found via Maps
        research = await research_company_tavily(lead['company_name'])
        enriched_leads.append({
            **lead,
            "research_summary": research.get("summary", "No details found.")
        })
    return enriched_leads

@mcp.tool()
async def process_and_email_lead(name: str, company: str, email: str, insights: str):
    """Saves lead to HubSpot and sends outreach email via Resend with full research details."""
    # 1. Sync to CRM with full insights
    crm_msg = await sync_to_hubspot(name, email, company, insights)
    
    # 2. Outreach with comprehensive email body including all Tavily research
    email_body = f"""
<h2>Sales Outreach for {company}</h2>

<p>Hi {name},</p>

<p>I came across your company and wanted to reach out based on some interesting insights:</p>

<div style="background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0;">
<pre style="white-space: pre-wrap; font-family: Arial, sans-serif;">{insights}</pre>
</div>

<p>I'd love to discuss how we can work together.</p>

<p>Best regards,<br>
Sales Team</p>
"""
    
    email_status = await send_sales_outreach(
        email_to=email,
        subject=f"Partnership Opportunity with {company}",
        body=email_body
    )
    
    return f"{crm_msg} | Outreach: {'Success' if email_status.get('id') else 'Failed'}"

if __name__ == "__main__":
    mcp.run()