import discord
from discord.ext import commands
import os
import time


OWNER_ID = 1042929958286266540  # CAMBIA ESTO POR TU ID DE DISCORD


class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()


    def is_owner(self, ctx):

        return ctx.author.id == OWNER_ID



    @discord.slash_command(
        name="botstatus",
        description="Ver estado del bot"
    )
    async def botstatus(self, ctx):

        if not self.is_owner(ctx):
            return await ctx.respond(
                "❌ No tienes permiso.",
                ephemeral=True
            )


        uptime = int(time.time() - self.start_time)

        await ctx.respond(
            f"""
🤖 **Estado del Bot**

🟢 Online
⏱️ Uptime: `{uptime}s`
📡 Ping: `{round(self.bot.latency*1000)}ms`
"""
        )



    @discord.slash_command(
        name="shutdown",
        description="Apagar bot"
    )
    async def shutdown(self, ctx):

        if not self.is_owner(ctx):
            return await ctx.respond(
                "❌ No tienes permiso.",
                ephemeral=True
            )


        await ctx.respond(
            "🔴 Apagando bot..."
        )

        await self.bot.close()



    @discord.slash_command(
        name="restart",
        description="Reiniciar bot"
    )
    async def restart(self, ctx):

        if not self.is_owner(ctx):
            return await ctx.respond(
                "❌ No tienes permiso.",
                ephemeral=True
            )


        await ctx.respond(
            "🔄 Reiniciando..."
        )


        os._exit(0)




def setup(bot):

    bot.add_cog(
        Owner(bot)
    )
