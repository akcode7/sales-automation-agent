import os

async def add_to_hubspot(name: str, email: str, company: str):
    """Add a lead to HubSpot CRM."""
    # Placeholder for actual HubSpot API POST request
    api_key = os.getenv("CRM_API_KEY")
    return f"Successfully synced {name} from {company} to CRM."