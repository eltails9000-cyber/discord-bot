import discord
from discord.ext import commands
import requests
import asyncio
from database import ban, check, unban
from config import API_URL, ROBLOX_KEY

class Roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def send_api_sync(self, endpoint, data):
        print(f"🚀 ENVIANDO A API: {endpoint} | {data}")
        try:
            response = requests.post(
                f"{API_URL}/{endpoint}",
                headers={"x-api-key": ROBLOX_KEY},
                json=data,
                timeout=10
            )
            print(f"📡 RESPUESTA API: {response.status_code} | {response.text[:200]}")
            return response.json() if response.ok else None
        except Exception as e:
            print(f"❌ ERROR API: {e}")
            return None

    async def send_api(self, endpoint, data):
        return await asyncio.to_thread(self.send_api_sync, endpoint, data)

    # ==================== COMANDOS ====================

    @discord.slash_command(name="robloxban", description="Banea jugador de Glory or Death")
    async def robloxban(self, ctx, userid: str, reason: str):
        await ctx.defer()
        try:
            ban(userid, reason, str(ctx.author))
            api = await self.send_api("ban", {"userid": userid, "reason": reason})
            status = "✅ Enviado a Roblox" if api and api.get("success") else "⚠️ API falló"

            await ctx.followup.send(f"""
🚫 **Roblox Ban**
**Usuario:** `{userid}`
**Razón:** {reason}
**Staff:** {ctx.author}
**Estado:** {status}
""")
        except Exception as e:
            print(f"❌ ERROR BAN: {e}")
            await ctx.followup.send("❌ Error ejecutando ban")

    @discord.slash_command(name="robloxcheck", description="Comprueba si un jugador está baneado")
    async def checkban(self, ctx, userid: str):
        await ctx.defer()
        result = check(userid)
        if result:
            await ctx.followup.send(f"""
🚫 **Está baneado**
**Usuario:** `{userid}`
**Razón:** {result.get('reason', 'Sin razón')}
**Staff:** {result.get('staff', 'Desconocido')}
""")
        else:
            await ctx.followup.send("✅ No tiene ban")

    @discord.slash_command(name="robloxunban", description="Quita un ban de Roblox")
    async def robloxunban(self, ctx, userid: str):
        await ctx.defer()
        try:
            unban(userid)
            api = await self.send_api("unban", {"userid": userid})
            status = "✅ Enviado a Roblox" if api and api.get("success") else "⚠️ API falló"

            await ctx.followup.send(f"""
✅ **Roblox Unban**
**Usuario:** `{userid}`
**Staff:** {ctx.author}
**Estado:** {status}
""")
        except Exception as e:
            print(f"❌ ERROR UNBAN: {e}")
            await ctx.followup.send("❌ Error ejecutando unban")

def setup(bot):
    bot.add_cog(Roblox(bot))
