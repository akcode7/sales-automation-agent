import httpx
import os

async def fetch_api(url: str, params: dict = None, headers: dict = None):
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()