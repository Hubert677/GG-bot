import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

print(f"DEBUG: DISCORD_TOKEN = {DISCORD_TOKEN}")
print(f"DEBUG: Dostępne zmienne: {list(os.environ.keys())[:10]}...")

if not DISCORD_TOKEN:
    print("⚠️  OSTRZEŻENIE: DISCORD_TOKEN nie jest ustawiony!")
    print("Bot się nie uruchomi bez tokenu")
    # Nie wyrzucamy błędu - pozwolimy botowi się uruchomić dla debugowania
    DISCORD_TOKEN = "placeholder"
