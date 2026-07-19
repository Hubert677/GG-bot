import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    print("⚠️  OSTRZEŻENIE: DISCORD_TOKEN nie jest ustawiony!")
    print("Bot się nie uruchomi bez tokenu")
    # Nie wyrzucamy błędu - pozwolimy botowi się uruchomić dla debugowania
    DISCORD_TOKEN = "placeholder"
