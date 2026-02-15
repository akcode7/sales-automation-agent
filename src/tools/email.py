import os
import httpx

async def send_sales_outreach(email_to: str, subject: str, body: str):
    """Sends a sales email using the Resend API."""
    api_key = os.getenv("EMAIL_API_KEY")
    if not api_key:
        raise ValueError("EMAIL_API_KEY environment variable is not set")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "from": "Sales Team <onboarding@resend.dev>", # Use your verified domain here
                "to": [email_to],
                "subject": subject,
                "html": body,  # Use body directly (already HTML formatted)
            }
        )
        return response.json()