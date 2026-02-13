import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

import events



load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(
    filename="discord.log",
    encoding="utf-8",
    mode="w"
)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

events.setup(bot)

async def main():
    async with bot:
        await bot.load_extension("commands.fun")
        await bot.load_extension("commands.ai")
        
        try:
            await bot.load_extension("commands.tts")
            print("✅ Cog TTS cargado")
        except Exception as e:
            print("❌ Error cargando cog:", e)
        
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())
