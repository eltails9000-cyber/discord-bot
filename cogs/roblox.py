import discord
from discord.ext import commands
import requests

from database import ban, check, unban
from config import API_URL, API_KEY


class Roblox(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    def send_api(self, endpoint, data):

        try:

            response = requests.post(

                f"{API_URL}/{endpoint}",

                headers={
                    "x-api-key": API_KEY
                },

                json=data,

                timeout=10

            )


            return response.json()


        except Exception as e:

            print(
                "[API ERROR]",
                e
            )

            return None



    @discord.slash_command(
        name="robloxban",
        description="Banea jugador de Glory or Death"
    )
    async def robloxban(
        self,
        ctx,
        userid: str,
        reason: str
    ):

        await ctx.defer()


        # Guardar local
        ban(
            userid,
            reason,
            str(ctx.author)
        )


        # Enviar a Roblox API
        api = self.send_api(

            "ban",

            {
                "userid": userid,
                "reason": reason
            }

        )


        if api and api.get("success"):

            status = "✅ Enviado a Roblox"

        else:

            status = "⚠️ Guardado local, API falló"



        await ctx.respond(

f"""
🚫 **Roblox Ban**

Usuario:
`{userid}`

Razón:
{reason}

Staff:
{ctx.author}

Estado:
{status}
"""

        )





    @discord.slash_command(
        name="robloxcheck",
        description="Comprueba si un jugador está baneado"
    )
    async def checkban(
        self,
        ctx,
        userid: str
    ):


        await ctx.defer()


        result = check(userid)


        if result:


            await ctx.respond(

f"""
🚫 **Está baneado**

Usuario:
`{userid}`

Razón:
{result['reason']}

Staff:
{result['staff']}
"""

            )


        else:


            await ctx.respond(
                "✅ No tiene ban"
            )







    @discord.slash_command(
        name="robloxunban",
        description="Quita un ban de Roblox"
    )
    async def robloxunban(
        self,
        ctx,
        userid: str
    ):


        await ctx.defer()


        # Base local
        unban(userid)



        # API Roblox
        api = self.send_api(

            "unban",

            {
                "userid": userid
            }

        )


        if api and api.get("success"):

            status = "✅ Enviado a Roblox"

        else:

            status = "⚠️ API falló"



        await ctx.respond(

f"""
✅ **Roblox Unban**

Usuario:
`{userid}`

Staff:
{ctx.author}

Estado:
{status}
"""

        )





def setup(bot):

    bot.add_cog(
        Roblox(bot)
    )
