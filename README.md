# GG-bot 🤖

Discord bot stworzony w Python z discord.py

## Instalacja

### Wymagania
- Python 3.8+
- pip

### Setup

1. Sklonuj repo:
```bash
git clone https://github.com/Hubert677/GG-bot.git
cd GG-bot
```

2. Stwórz virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

4. Stwórz plik `.env`:
```bash
cp .env.example .env
```

5. Wstaw token bota do `.env`:
```
DISCORD_TOKEN=your_discord_token_here
PREFIX=!
```

6. Uruchom bota:
```bash
python main.py
```

## Deployment na Render

1. Stwórz repo na GitHub
2. Połącz je z Render
3. Ustaw zmienne środowiskowe na Render (Settings → Environment)
4. Deploy!

## Komendy

### 📌 Ogólne
- `!ping` - Sprawdź latencję bota
- `!help` - Pokaż listę wszystkich komend
- `!info` - Informacje o bocie

### 🎫 Tickety
- `!create-ticket [powód]` - Stwórz nowy ticket
- `!close-ticket` - Zamknij ticket **(ADMIN)**

### 👋 Powitania/Pożegnania
- `!set-welcome [wiadomość]` - Ustaw wiadomość powitania **(ADMIN)**
- `!set-goodbye [wiadomość]` - Ustaw wiadomość pożegnania **(ADMIN)**

### 🔨 Moderacja
- `!ban @user [powód]` - Zbanuj użytkownika **(ADMIN)**
- `!kick @user [powód]` - Wyrzuć użytkownika **(ADMIN)**
- `!warn @user [powód]` - Ostrzeż użytkownika **(ADMIN)**
- `!clear [ilość]` - Usuń wiadomości **(ADMIN)**

## Struktura projektu

```
.
├── main.py                      # Główny plik bota
├── config.py                    # Konfiguracja
├── cogs/                        # Folder z komendami
│   ├── ping.py                  # Komenda ping
│   ├── info.py                  # Komendy help, info
│   ├── welcome.py               # Powitania/Pożegnania
│   ├── tickets.py               # System ticketów
│   └── moderation.py            # Ban, kick, warn, clear
├── welcome_config.json          # Konfiguracja powitań (auto)
├── tickets_config.json          # Konfiguracja ticketów (auto)
├── requirements.txt             # Zależności
├── .env.example                 # Template zmiennych
├── Procfile                     # Dla Render
└── README.md                    # Ten plik
```

## Dodawanie nowych komend

Tworz nowe pliki w folderze `cogs/` i implementuj komendę jako Cog.

Przykład w `cogs/ping.py`