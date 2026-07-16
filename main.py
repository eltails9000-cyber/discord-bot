import discord
from config import TOKEN

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


# Cargar comandos
bot.load_extension("cogs.roblox")
bot.load_extension("cogs.owner")
bot.load_extension("cogs.maintenance")
bot.load_extension("cogs.moderation")

# Iniciar bot
bot.run(TOKEN)
