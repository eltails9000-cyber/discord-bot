import os
from dotenv import load_dotenv

load_dotenv()

# Discord
TOKEN = os.getenv("DISCORD_TOKEN")

# Roblox API
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("ROBLOX_API_KEY") or os.getenv("API_KEY")

# Owner
OWNER_ID = 1042929958286266540

# Debug
print("🔧 Config cargada:")
print(f"API_URL     → {'✅' if API_URL else '❌'}")
print(f"API_KEY     → {'✅' if API_KEY else '❌'}")
print(f"TOKEN       → {'✅' if TOKEN else '❌'}")
