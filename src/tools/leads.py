import os
import httpx
from src.utils import fetch_api

async def search_leads_serp(query: str):
    """Search for lead contact info using SerpApi."""
    api_key = os.getenv("SERPAPI_API_KEY")
    params = {
        "engine": "google",
        "q": f"{query} email linkedin",
        "api_key": api_key
    }
    data = await fetch_api("https://serpapi.com/search", params=params)
    results = data.get("organic_results", [])
    return [{"title": r.get("title"), "link": r.get("link"), "snippet": r.get("snippet")} for r in results[:3]]

async def research_company_tavily(company_name: str):
    """Perform deep AI research on a company using Tavily."""
    api_key = os.getenv("TAVILY_API_KEY")
    payload = {
        "api_key": api_key,
        "query": f"latest business news and tech stack for {company_name}",
        "search_depth": "advanced"
    }
    async with httpx.AsyncClient() as client:
        res = await client.post("https://api.tavily.com/search", json=payload)
        return res.json().get("results", [])