import os, httpx

async def sync_to_hubspot(name: str, email: str, company: str, notes: str):
    """Upsert logic: Updates if exists, creates if not."""
    api_key = os.getenv("CRM_API_KEY")
    if not api_key:
        raise ValueError("CRM_API_KEY environment variable is not set")
    
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    # 1. Search by email first
    search_url = "https://api.hubapi.com/crm/v3/objects/contacts/search"
    search_query = {"filterGroups": [{"filters": [{"propertyName": "email", "operator": "EQ", "value": email}]}]}
    
    async with httpx.AsyncClient() as client:
        s_res = await client.post(search_url, headers=headers, json=search_query)
        found = s_res.json().get("results", [])
        
        payload = {"properties": {"email": email, "firstname": name, "company": company, "notes": notes}}
        
        if found:
            # Update existing
            contact_id = found[0]["id"]
            await client.patch(f"https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}", headers=headers, json=payload)
            return f"✅ Updated existing lead: {name}"
        else:
            # Create new
            await client.post("https://api.hubapi.com/crm/v3/objects/contacts", headers=headers, json=payload)
            return f"🌟 Created new lead: {name}"