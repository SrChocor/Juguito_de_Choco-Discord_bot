import discord
from discord.ext import commands
from AI.openrouter import ask_ai
from AI.stable_horde import generate_image
import urllib.parse 


class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="preg")
    async def preg(self, ctx, *, prompt: str):
        thinking = await ctx.send("🤖 Pensando...")
        response = await ask_ai(prompt)
            
        if len(response) > 2000:
                response = response[:2000] + "\n\n..."
            
            
        await thinking.edit(content=response)
            
    @commands.command(name="img")
    async def img(self, ctx, *, prompt: str):
        await ctx.message.delete()

        status = await ctx.send("Generando imagen, pere tantico que soy gratis")

        try:
            image_url = await generate_image(prompt)

            embed = discord.Embed(
                title="🖼️ AI Generated Image",
                description=f"**Prompt:** {prompt}",
                color=0x2F3136
            )
            embed.set_image(url=image_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}")

            await status.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            await status.edit(content="❌ Failed to generate image.")
            
            
async def setup(bot):
    await bot.add_cog(AI(bot))