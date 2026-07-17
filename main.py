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


bot = GloryBot()
