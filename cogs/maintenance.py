import discord
from discord.ext import commands

from utils import maintenance_state


OWNER_ID = 1042929958286266540  # TU ID


class Maintenance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.slash_command(
        name="maintenance",
        description="Activar o desactivar mantenimiento"
    )
    async def maintenance(
        self,
        ctx,
        mode: discord.Option(
            str,
            choices=["on", "off"]
        )
    ):

        if ctx.author.id != OWNER_ID:
            return await ctx.respond(
                "❌ Sin permisos.",
                ephemeral=True
            )


        if mode == "on":

            maintenance_state.maintenance_mode = True

            await ctx.respond(
                "🔴 **Modo mantenimiento activado**\n"
                "Los comandos normales están bloqueados."
            )


        else:

            maintenance_state.maintenance_mode = False

            await ctx.respond(
                "🟢 **Modo mantenimiento desactivado**\n"
                "El bot vuelve a funcionar."
            )



def setup(bot):
    bot.add_cog(Maintenance(bot))


def setup(bot):

    bot.add_cog(
        Maintenance(bot)
    )
