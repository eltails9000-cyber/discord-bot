import discord
from discord.ext import commands


OWNER_ID = 1042929958286266540  # Cambia por tu ID


maintenance_mode = False


class Maintenance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    def is_owner(self, ctx):
        return ctx.author.id == OWNER_ID



    @discord.slash_command(
        name="maintenance",
        description="Controla el modo mantenimiento"
    )
    async def maintenance(
        self,
        ctx,
        mode: discord.Option(
            str,
            choices=[
                "on",
                "off"
            ]
        )
    ):

        global maintenance_mode


        if not self.is_owner(ctx):
            return await ctx.respond(
                "❌ No tienes permiso.",
                ephemeral=True
            )


        if mode == "on":

            maintenance_mode = True

            await ctx.respond(
                "🔴 **Modo mantenimiento activado**\n"
                "Los comandos normales están bloqueados."
            )


        else:

            maintenance_mode = False

            await ctx.respond(
                "🟢 **Modo mantenimiento desactivado**\n"
                "El bot vuelve a funcionar."
            )



def setup(bot):

    bot.add_cog(
        Maintenance(bot)
    )
