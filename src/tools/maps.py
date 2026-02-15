import os, httpx

async def find_businesses_on_maps(query: str, location: str):
    """Finds business leads using the Google Places API (New)."""
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_MAPS_API_KEY environment variable is not set")
    url = "https://places.googleapis.com/v1/places:searchText"
    
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        # Field Masking saves you money: only ask for what you need
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.websiteUri"
    }
    
    # We combine the industry and city for a powerful search
    data = {"textQuery": f"{query} in {location}"}
    
    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers, json=data)
        
        # Check for API errors
        if res.status_code != 200:
            error_msg = res.json().get("error", {}).get("message", "Unknown error")
            raise ValueError(f"Google Maps API error: {error_msg} (Status: {res.status_code})")
        
        places = res.json().get("places", [])
        
        # If no places found, raise error instead of returning empty
        if not places:
            raise ValueError(f"No businesses found for '{query}' in {location}. Try a different search.")
        
        return [{
            "company_name": p.get("displayName", {}).get("text"),
            "address": p.get("formattedAddress"),
            "website": p.get("websiteUri", "N/A")
        } for p in places[:5]] # Top 5 leads