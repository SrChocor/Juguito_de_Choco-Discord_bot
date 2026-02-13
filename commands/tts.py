from enum import member
import discord
from discord.ext import commands
from gtts import gTTS
import asyncio
import os


class TTS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.owner_id  = None
        self.vc = None
        self.file = "tts.mp3"
        self.text_channel = None
        
        # Generte the speak function
        
    async def speak(self, text):
        
        try:
            loop = asyncio.get_event_loop()
            tts = await loop.run_in_executor(None, lambda: gTTS(text=text, lang="es", slow=False))
            await loop.run_in_executor(None, lambda: tts.save(self.file))

            while self.vc.is_playing():
                await asyncio.sleep(0.5)
                
            if self.vc and self.vc.is_connected():
                self.vc.play(discord.FFmpegPCMAudio(self.file))
            else:
                print("No estoy conectado a un canal de voz.")
                
        except asyncio.TimeoutError:
            print("Error: La generación de TTS tomó demasiado tiempo.")
            if self.text_channel:
                await self.text_channel.send("⏳ La generación de TTS tomó demasiado tiempo, intenta de nuevo, es que mi dueño es medio menor.")
        except Exception as e:
            print (f"Error al reproducir TTS: {e}")
            if self.text_channel:
                await self.text_channel.send("❌ Ocurrió un error al reproducir el TTS, intenta de nuevo, es que mi dueño es medio menor.")
            
    """  
    @commands.command()
    async def ping(self, ctx):
            await ctx.send("pong")
    """
        
    @commands.command()
        
    async def voz(self, ctx, *, text: str):
        if not ctx.author.voice:
            await ctx.send("Debes estar en un canal de voz.")
            return

        if self.owner_id is None:
            self.owner_id = ctx.author.id
            self.text_channel = ctx.channel
            await ctx.send(f"Control asignado a {ctx.author.mention} para hablar como un ppy.")
        elif ctx.author.id != self.owner_id:
            await ctx.send(f"Toi ocupado con {self.bot.get_user(self.owner_id).mention} menor.")
            return
     
        channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            self.vc = await channel.connect()
        else:
            self.vc = ctx.voice_client
            if self.vc.channel != channel:
                await self.vc.move_to(channel)

        await self.speak(text)

    @commands.command()
    async def salir(self, ctx):
        if ctx.author.id != self.owner_id:
            await ctx.send(f"Pailas mi papacho solo el que me pidio puede desconectarme.")
            return

        if ctx.voice_client:
            await ctx.voice_client.disconnect()

        self.owner_id = None
        self.vc = None
        self.text_channel = None

        if os.path.exists(self.file):
            os.remove(self.file)

        await ctx.send("Me piro vampiro, lsito para otro uso.")
        
    async def cleanup(self):
        """Helper function to clean up bot state"""
        try:
            if self.vc:
            #stop if playing
                if self.vc.is_playing():
                    self.vc.stop()
            
            await self.vc.disconnect()
        
            self.owner_id = None
            self.vc = None
            self.text_channel = None
        
            if os.path.exists(self.file):
                os.remove(self.file)
            
        except Exception as e:
            print(f"Error during cleanup: {e}")
            self.owner_id = None
            self.vc = None
            self.text_channel = None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

    # Check if the owner changed voice channels
        if member.id == self.owner_id and self.vc:
            
        # Owner left voice completely and disconnect
            if after.channel is None:
                if self.text_channel:
                    await self.text_channel.send(f"{self.bot.get_user(self.owner_id).mention} se desconecto del canal de voz, me piro tambien.")
                await self.cleanup()
        # Owner moved to a different channel and follow them
            elif after.channel != self.vc.channel:
                if self.text_channel:
                    await self.text_channel.send(f"{self.bot.get_user(self.owner_id).mention} se movio a otro canal, sigo al menor.")
                await self.vc.move_to(after.channel)
                    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author.bot:
            return

        ctx = await self.bot.get_context(message)
        #if is a valid command, do nothing and let the command handler process it
        if ctx.valid:
            return

        # automatic reading for the owner without prefix
        if (
            self.owner_id == message.author.id
            and self.vc
            and message.content
            and not message.content.startswith("!")
        ):
            await self.speak(message.content)
            
async def setup(bot):
    await bot.add_cog(TTS(bot))
           
            
            