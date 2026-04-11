from enum import member
from pydoc import text
import discord
from discord import channel
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
            print(f"[SPEAK] Generating TTS for: {text}")
            loop = asyncio.get_event_loop()
            tts = await loop.run_in_executor(None, lambda: gTTS(text=text, lang="es", slow=False))
            print(f"[SPEAK] gTTS object created")
        
            await loop.run_in_executor(None, lambda: tts.save(self.file))
            print(f"[SPEAK] File saved, exists={os.path.exists(self.file)}, size={os.path.getsize(self.file) if os.path.exists(self.file) else 0}")

            while self.vc and self.vc.is_connected() and self.vc.is_playing():
                await asyncio.sleep(0.5)
            
            print(f"[SPEAK] vc={self.vc}, connected={self.vc.is_connected() if self.vc else None}")
        
            if self.vc and self.vc.is_connected():
                print("[SPEAK] Calling vc.play()")
                def after_playing(error):
                    if error:
                        print(f"[PLAY] Error: {os.error}")

                self.vc.play(discord.FFmpegPCMAudio(self.file), after=after_playing)
                print("[SPEAK] vc.play() called successfully")
            else:
                print("[SPEAK] Not connected!")
            
        except Exception as e:
            import traceback
            print(f"[SPEAK] Exception: {e}")
            traceback.print_exc()

    @commands.command()
    async def voz(self, ctx, *, text: str):
        if not ctx.author.voice:
            await ctx.send("Debes estar en un canal de voz.")
            return

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect(force=True)
            await asyncio.sleep(1)
        
        if self.owner_id is None:
            self.owner_id = ctx.author.id
            self.text_channel = ctx.channel
            await ctx.send(f"Control asignado a {ctx.author.mention}")
        elif ctx.author.id != self.owner_id:
            await ctx.send(f"Toi ocupado.")
            return

        channel = ctx.author.voice.channel

    # Generate TTS FIRST before connecting to voice
        print("[VOZ] Generating TTS before connecting...")
        loop = asyncio.get_event_loop()
        tts = await loop.run_in_executor(None, lambda: gTTS(text=text, lang="es", slow=False))
        await loop.run_in_executor(None, lambda: tts.save(self.file))
        print(f"[VOZ] TTS ready, connecting now...")

    # NOW connect to voice
        if ctx.voice_client is None:
            self.vc = await channel.connect(reconnect=False)
        else:
            self.vc = ctx.voice_client
            if self.vc.channel != channel:
                await self.vc.move_to(channel)

    # Play immediately after connecting
        if self.vc and self.vc.is_connected():
            def after_playing(error):
                    if error:
                        print(f"[PLAY] Error: {os.error}")

            self.vc.play(discord.FFmpegPCMAudio(self.file), after=after_playing)
                
        else:
            await ctx.send("No pude conectarme al canal de voz.")
    
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
        print(f"Voice update: {member} | before: {before.channel} | after: {after.channel} | owner_id: {self.owner_id} | member.id: {member.id}")
        
        if member.id == self.bot.user.id:
            return
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
           
            
            