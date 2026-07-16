import discord
import requests
import os


TOKEN=os.getenv(
    "DISCORD_TOKEN"
)


API=os.getenv(
    "API_URL"
)


intents=discord.Intents.all()


bot=discord.Bot(
    intents=intents
)



@bot.event
async def on_ready():

    print(
        f"Bot conectado {bot.user}"
    )



@bot.slash_command(
    name="banroblox",
    description="Banea un jugador de Roblox"
)
async def banroblox(
    ctx,
    userid:str,
    reason:str
):

    requests.post(
        API+"/ban",
        json={
            "userid":userid,
            "reason":reason
        }
    )


    await ctx.respond(
        "Jugador baneado correctamente"
    )



bot.run(TOKEN)
