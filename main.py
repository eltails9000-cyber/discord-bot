import discord
from discord.ext import commands

from config import TOKEN
from utils import maintenance_state
from utils.permissions import owner_check

print("🚀 Iniciando bot...")


class GloryBot(commands.Bot):

    def __init__(self):

        intents = discord.Intents.all()

        super().__init__(
            command_prefix="!",
            intents=intents
        )


    async def setup_hook(self):

        print("📦 Cargando comandos...")

        extensions = [
            "cogs.roblox",
            "cogs.owner",
            "cogs.maintenance",
            "cogs.moderation"
        ]

        for extension in extensions:
            try:
                await self.load_extension(extension)
                print(f"✅ Cargado: {extension}")

            except Exception as e:
                print(f"❌ Error cargando {extension}: {e}")


        print("🔄 Sincronizando comandos...")

        await self.tree.sync()

        print("✅ Comandos sincronizados")



bot = GloryBot()


# Permiso global OWNER
bot.add_check(owner_check)


async def maintenance_check(ctx):

    allowed_commands = [
        "maintenance",
        "botstatus",
        "restart",
        "shutdown"
    ]


    if (
        maintenance_state.maintenance_mode
        and ctx.command
        and ctx.command.name not in allowed_commands
    ):

        await ctx.send(
            "🔴 **Bot en mantenimiento.**\nIntenta más tarde.",
            ephemeral=True
        )

        return False


    return True



bot.add_check(maintenance_check)



@bot.event
async def on_ready():

    print("🔥 Evento on_ready ejecutado")


    await bot.change_presence(
        status=discord.Status.dnd,

        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Glory or Death"
        )
    )


    print(f"✅ Online como {bot.user}")



if __name__ == "__main__":

    try:

        bot.run(TOKEN)

    except Exception as e:

        print(
            f"❌ Error crítico iniciando bot: {e}"
        )
