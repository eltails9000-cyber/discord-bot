import discord
from discord.ext import commands
import asyncio
import requests

from database import ban, check, unban
from config import API_URL, ROBLOX_KEY


class Roblox(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    def send_api_sync(self, endpoint, data):

        print(f"🚀 API REQUEST: {endpoint} | {data}")

        try:

            response = requests.post(
                f"{API_URL}/{endpoint}",
                headers={
                    "x-api-key": ROBLOX_KEY
                },
                json=data,
                timeout=10
            )


            print(
                f"📡 API RESPONSE: {response.status_code} | {response.text[:200]}"
            )


            if response.ok:
                return response.json()

            return None


        except Exception as e:

            print(f"❌ API ERROR: {e}")
            return None



    async def send_api(self, endpoint, data):

        return await asyncio.to_thread(
            self.send_api_sync,
            endpoint,
            data
        )



    # =========================
    # ROBLOX BAN
    # =========================

    @discord.app_commands.command(
        name="robloxban",
        description="Banea jugador de Glory or Death"
    )
    async def robloxban(
        self,
        interaction: discord.Interaction,
        userid: str,
        reason: str
    ):

        await interaction.response.defer()


        try:

            ban(
                userid,
                reason,
                str(interaction.user)
            )


            api = await self.send_api(
                "ban",
                {
                    "userid": userid,
                    "reason": reason
                }
            )


            status = (
                "✅ Enviado a Roblox"
                if api and api.get("success")
                else "⚠️ API falló"
            )


            await interaction.followup.send(
f"""
🚫 **Roblox Ban**

👤 Usuario:
`{userid}`

📝 Razón:
{reason}

🛡️ Staff:
{interaction.user}

📡 Estado:
{status}
"""
            )


        except Exception as e:

            print(f"❌ ERROR BAN: {e}")

            await interaction.followup.send(
                "❌ Error ejecutando ban"
            )



    # =========================
    # CHECK BAN
    # =========================

    @discord.app_commands.command(
        name="robloxcheck",
        description="Comprueba si un jugador está baneado"
    )
    async def robloxcheck(
        self,
        interaction: discord.Interaction,
        userid: str
    ):

        await interaction.response.defer()


        result = check(userid)


        if result:

            await interaction.followup.send(
f"""
🚫 **Jugador baneado**

👤 Usuario:
`{userid}`

📝 Razón:
{result.get("reason","Sin razón")}

🛡️ Staff:
{result.get("staff","Desconocido")}
"""
            )

        else:

            await interaction.followup.send(
                "✅ No tiene ban"
            )



    # =========================
    # UNBAN
    # =========================

    @discord.app_commands.command(
        name="robloxunban",
        description="Quita un ban de Roblox"
    )
    async def robloxunban(
        self,
        interaction: discord.Interaction,
        userid: str
    ):

        await interaction.response.defer()


        try:

            unban(userid)


            api = await self.send_api(
                "unban",
                {
                    "userid": userid
                }
            )


            status = (
                "✅ Enviado a Roblox"
                if api and api.get("success")
                else "⚠️ API falló"
            )


            await interaction.followup.send(
f"""
✅ **Roblox Unban**

👤 Usuario:
`{userid}`

🛡️ Staff:
{interaction.user}

📡 Estado:
{status}
"""
            )


        except Exception as e:

            print(f"❌ ERROR UNBAN: {e}")

            await interaction.followup.send(
                "❌ Error ejecutando unban"
            )



async def setup(bot):

    await bot.add_cog(
        Roblox(bot)
    )
