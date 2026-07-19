import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise ValueError(
        "❌ DISCORD_TOKEN nie jest ustawiony!\n"
        "Na Render: ustaw zmienną w Environment Variables\n"
        "Lokalnie: utwórz plik .env z DISCORD_TOKEN=twoj_token"
    )
