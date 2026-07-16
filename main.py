import discord

from config import TOKEN
from utils import maintenance_state
from utils.permissions import owner_check


print("🚀 Iniciando bot...")


intents = discord.Intents.all()


bot = discord.Bot(
    intents=intents
)


print("✅ Bot creado")


bot.add_check(owner_check)



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

    await bot.sync_commands()

    print("✅ Comandos sincronizados")



async def maintenance_check(ctx):

    allowed_commands = [
        "maintenance",
        "botstatus",
        "restart",
        "shutdown"
    ]

    if maintenance_state.maintenance_mode:

        if ctx.command.name not in allowed_commands:

            await ctx.respond(
                "🔴 **Bot en mantenimiento.**\nIntenta más tarde.",
                ephemeral=True
            )

            return False

    return True



bot.add_check(maintenance_check)



print("📦 Cargando comandos...")


bot.load_extension("cogs.roblox")
bot.load_extension("cogs.owner")
bot.load_extension("cogs.maintenance")
bot.load_extension("cogs.moderation")


print("✅ Cogs cargados")


bot.run(TOKEN)
