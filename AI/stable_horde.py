import aiohttp
import os
import asyncio

HORDE_API_KEY = os.getenv("HORDE_API_KEY", "0000000000")

BASE_URL = "https://stablehorde.net/api/v2"

async def generate_image(prompt: str) -> str:
    headers = {
        "apikey": HORDE_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "params": {
            "sampler_name": "k_euler",
            "steps": 20,
            "cfg_scale": 7,
            "width": 512,
            "height": 512
        },
        "nsfw": False,
        "models": ["stable_diffusion", "AlbedoBase XL 3.1", "AbsoluteReality"],
        "r2": True
    }

    async with aiohttp.ClientSession() as session:
        # Submit job
        async with session.post(f"{BASE_URL}/generate/async", json=payload, headers=headers) as resp:
            data = await resp.json()
            request_id = data["id"]

        # Poll result
        while True:
            await asyncio.sleep(3)
            async with session.get(f"{BASE_URL}/generate/status/{request_id}") as status:
                status_data = await status.json()

                if status_data["done"]:
                    return status_data["generations"][0]["img"]