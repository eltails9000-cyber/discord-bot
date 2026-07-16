import discord
from config import TOKEN

from utils import maintenance_state


intents = discord.Intents.all()


bot = discord.Bot(
    intents=intents
)


@bot.event
async def on_ready():

    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="Glory or Death"
        )
    )

    print(f"✅ Online como {bot.user}")

    await bot.sync_commands()



@bot.event
async def on_application_command(ctx):

    command = ctx.command.name


    # Comandos que siguen funcionando en mantenimiento
    allowed_commands = [
        "maintenance",
        "botstatus",
        "restart",
        "shutdown"
    ]


    if maintenance_state.maintenance_mode:

        if command not in allowed_commands:

            await ctx.respond(
                "🔴 **Bot en mantenimiento.**\n"
                "Intenta más tarde.",
                ephemeral=True
            )

            raise discord.CheckFailure



# Cargar comandos
bot.load_extension("cogs.roblox")
bot.load_extension("cogs.owner")
bot.load_extension("cogs.maintenance")
bot.load_extension("cogs.moderation")


# Iniciar bot
bot.run(TOKEN)
