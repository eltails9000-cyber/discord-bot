import os
from dotenv import load_dotenv

load_dotenv()

# Discord
TOKEN = os.getenv("DISCORD_TOKEN")

# Roblox API
API_URL = os.getenv("API_URL")
ROBLOX_KEY = os.getenv("ROBLOX_API_KEY")

# Owner
OWNER_ID = 1042929958286266540

# Debug
print("🔧 Config cargada:")
print(f"ROBLOX_KEY  → {'✅' if ROBLOX_KEY else '❌'}")
print(f"TOKEN       → {'✅' if TOKEN else '❌'}")
