from discord.ext import commands
import discord

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def baretiana(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title=f"{ctx.author.name} lo pegó con baretiana",
            color=0x00ff00
        )
        embed.set_image(
            url="https://cdn-longterm.mee6.xyz/plugins/commands/images/549029739621384215/6884b5723580d3a1d21b640d4ac13edce31ae88354204280781f09ed5172dd06.jpeg"
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def chamba(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title=f"{ctx.author.name} anda chambiando, no molestar."
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/755281198539997265/963154936386961428/unknown.png"
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def margo(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title=f"{ctx.author.name} presentó sus pornolensias",
            description="R.I.P Margo bareta 🕊️"
        )
        embed.set_image(
            url="https://media.discordapp.net/attachments/748228006765527211/908421722322133072/baremargo1.jpg"
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def margop(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title=f"{ctx.author.name} brindó con las animas benditas",
            color=0xff0000
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/755281198539997265/941117209609117726/IMG-20220206-WA0002.jpg"
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def paz(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title=f"{ctx.author.name} llama a la paz",
            color=0xff0000
        )
        embed.set_image(
            url="https://images7.memedroid.com/images/UPLOADED879/608f64bdaf8bb.jpeg"
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def piro(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title="No sea sapo piro",
            color=0xff0000
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/900113455279906897/1467744483952037959/7a54ee2ac50a2d2542a5b445faaf2a16.png"
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def nao(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title="Ñao Ñao menor",
            color=0xff0000
        )
        embed.set_image(
            url="https://pbs.twimg.com/media/EyZAbsoWUAEgFG9.jpg"
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def gracias(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title=f"{ctx.author.name} se lo engrandece",
            color=0xff0000
        )
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/900113455279906897/1467987178977099932/E8ObeYKWUAgWn3t.png"
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def it(self, ctx):
        await ctx.message.delete()
        await ctx.send(
            "https://cdn.discordapp.com/attachments/791408958803673088/1450679616631996416/image.png"
        )


    @commands.command()
    async def script(self, ctx):
        await ctx.message.delete()
        await ctx.author.send("Esto es informacion privilegiada, usela bien.")
        await ctx.author.send(
            "https://cdn.discordapp.com/attachments/900113455279906897/1467718725774872703/image.png"
        )

async def setup(bot):
    await bot.add_cog(Fun(bot))
