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
        print("🚀 ENVIANDO A API:", endpoint, data)
        try:
            response = requests.post(
                f"{API_URL}/{endpoint}",
                headers={"x-api-key": ROBLOX_KEY},
                json=data,
                timeout=5
            )
            print("📡 RESPUESTA API:", response.status_code, response.text)
            return response.json()
        except Exception as e:
            print("❌ ERROR API:", e)
            return None

    async def send_api(self, endpoint, data):
        return await asyncio.to_thread(self.send_api_sync, endpoint, data)

    # ... (el resto de tus comandos se mantienen igual)
