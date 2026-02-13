from email import message
from IPython import embed
from discord.ext import commands
import discord

def setup(bot: commands.Bot):

    # BOT READY

    @bot.event
    async def on_ready():
        print(f"Ready pa la guerra mi papacho ")



    # new member welcome 

    @bot.event
    async def on_member_join(member: discord.Member):
        try:
            await member.send(f"Se coló, {member.name}, pilas ahí!")
        except discord.Forbidden:
            pass  # el usuario tiene DMs cerrados



    # message checks, always looking at messages

    @bot.event
    async def on_message(message: discord.Message):

        # ignorar bots
        if message.author.bot:
            return

        content = message.content.lower()

        # keywords automáticos
        if "ppy" in content:
            await message.channel.send(
                f"{message.author.mention} ALERTA DE PPY"
            )

        if "joc" in content:
            embed = discord.Embed(description="Joc\n\nq:v")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/900113455279906897/1467606441971154997/51ahghn0wmo71.png"
                    )
            await message.channel.send(embed=embed)

        if "adihlio" in content:
            await message.channel.send("andan mencionando a mi papi?")
            await message.channel.send(
                "https://cdn.discordapp.com/attachments/1467598210200506571/1467746942191669309/adihlio.png"
            )

        # michis
        if message.author.id == 1200508372642975795:
            await message.add_reaction("✨")
        '''
        #misha    
        if message.author.id == :
            await message.add_reaction("🍆")
            await message.add_reaction("🫄")
         '''
        
        await bot.process_commands(message)



    # error handling for commands
    @bot.event
    async def on_command_error(ctx, error):
        
        # if has a cooldown
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("⏳ Espere un poco antes de volver a usar este comando.")
            return
        
        # missing arguments
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("❌ Faltan argumentos para este comando.")
            return

        # Unknown command
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("❌ Qué comando trata de usar mi papacho? escriba bien.")
            return  

        # other errors
        print(f"Error inesperado: {error}")
