import os
import httpx

async def research_company_tavily(company_name: str):
    """Deep search for company news and key decision makers."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY environment variable is not set")
    
    # We craft the query to explicitly look for leadership
    query = f"Who are the key decision makers at {company_name}? Also find recent business news."
    
    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "advanced",
        "include_answer": True # This gives the AI a direct summary
    }
    
    async with httpx.AsyncClient() as client:
        res = await client.post("https://api.tavily.com/search", json=payload)
        data = res.json()
        
        # Tavily's "answer" field is gold for LLMs
        return {
            "summary": data.get("answer"),
            "raw_results": data.get("results", [])[:5]
        }