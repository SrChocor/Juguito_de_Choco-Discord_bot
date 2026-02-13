import aiohttp
import os

open_api_key = os.getenv("OPENROUTER_API_KEY")

API_url = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "arcee-ai/trinity-large-preview:free"

async def ask_ai(prompt: str) -> str:
    headers = {"authorization": f"Bearer {open_api_key}",
               "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "DiscordBot"
               }
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful Discord bot. Be concise."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 300
        # no reasoning, just answer, discord bot
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(API_url, headers=headers, json=payload) as resp:
            if resp.status != 200:
                return "❌ AI service error."

            data = await resp.json()
            return data["choices"][0]["message"]["content"]
        
        