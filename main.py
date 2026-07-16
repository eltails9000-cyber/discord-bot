import discord
import os


from config import TOKEN


intents = discord.Intents.all()


bot = discord.Bot(
    intents=intents
)



@bot.event
async def on_ready():

    print(
        f"✅ Online como {bot.user}"
    )

    await bot.sync_commands()



# cargar comandos

bot.load_extension(
    "cogs.roblox"
)

 bot.load_extension(
     "cogs.moderation"
 )



bot.run(TOKEN)
