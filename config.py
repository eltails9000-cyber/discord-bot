import os

# Discord
TOKEN = os.getenv("DISCORD_TOKEN")

# Roblox API (usando las variables que tienes)
API_URL = os.getenv("API_URL")
ROBLOX_KEY = os.getenv("ROBLOX_API_KEY") or os.getenv("API_KEY")  # por si acaso

# Owner
OWNER_ID = 1042929958286266540

# Debug (para que veas si se cargan)
print("🔧 Config cargada:")
print(f"API_URL: {'✅' if API_URL else '❌'}")
print(f"ROBLOX_KEY: {'✅' if ROBLOX_KEY else '❌'}")
