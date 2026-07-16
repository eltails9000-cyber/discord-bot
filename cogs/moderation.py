import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.slash_command(
        name="testmod",
        description="Prueba moderación"
    )
    async def testmod(self, ctx):

        await ctx.respond(
            "✅ Sistema de moderación funcionando"
        )


def setup(bot):
    bot.add_cog(
        Moderation(bot)
    )
