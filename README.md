# GG-bot 🤖

Discord bot stworzony w Python z discord.py - **35+ komend** dla pełnego serwera!

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

## Komendy - Pełna Lista

**Wszystkie komendy są slash komendami** (`/`)

### 📌 Ogólne
- `/ping` - Sprawdź latencję bota
- `/help` - Pokaż listę wszystkich komend
- `/info` - Informacje o bocie
- `/user [użytkownik]` - Informacje o użytkowniku
- `/server` - Informacje o serwerze
- `/avatar [użytkownik]` - Pokaż avatar użytkownika
- `/stats` - Statystyki serwera
- `/botinfo` - Szczegółowe info o bocie
- `/guildinfo` - Szczegółowe info o serwerze
- `/members` - Liczba członków i statystyki
- `/uptime` - Jak długo bot działa

### 🎮 Zabawa & Gry
- `/8ball [pytanie]` - Magiczna kula 8 🔮
- `/coin` - Rzut monetą 🪙
- `/dice [ścian]` - Rzut kostką d20 (domyślnie) 🎲
- `/joke` - Losowy kawał 😂
- `/rps [papier|kamień|nożyce]` - Papier, Kamień, Nożyce 🎮

### 🏷️ Zarządzanie Rolami
- `/role-add [użytkownik] [rola]` - Dodaj rolę (ADMIN)
- `/role-remove [użytkownik] [rola]` - Usuń rolę (ADMIN)
- `/role-list` - Pokaż wszystkie role na serwerze
- `/myroles` - Pokaż swoje role

### 📊 Statystyki & XP
- `/profile [użytkownik]` - Pokaż profil użytkownika
- `/leaderboard` - Top 10 użytkowników
- `/topstats` - Top 5 aktywnych
- `/addxp [użytkownik] [ilość]` - Dodaj XP (ADMIN)

### 🎫 System Ticketów
- `/create-ticket [powód]` - Stwórz nowy ticket
- `/close-ticket` - Zamknij ticket (ADMIN)

### 👋 Powitania/Pożegnania
- `/set-welcome [wiadomość]` - Ustaw wiadomość powitania (ADMIN)
- `/set-goodbye [wiadomość]` - Ustaw wiadomość pożegnania (ADMIN)

### 🔨 Moderacja
- `/ban [użytkownik] [powód]` - Zbanuj użytkownika (ADMIN)
- `/kick [użytkownik] [powód]` - Wyrzuć użytkownika (ADMIN)
- `/warn [użytkownik] [powód]` - Ostrzeż użytkownika (ADMIN)
- `/clear [ilość]` - Usuń wiadomości (ADMIN)
- `/slowmode [sekundy]` - Ustaw tryb powolny kanału (ADMIN)

## Struktura projektu

```
.
├── main.py                      # Główny plik bota
├── config.py                    # Konfiguracja
├── cogs/                        # Folder z komendami
│   ├── info.py                  # Komendy help, info, ping
│   ├── slash_commands.py        # Dodatkowe komendy info
│   ├── fun.py                   # Komendy zabawy (8ball, dice, etc)
│   ├── roles.py                 # Zarządzanie rolami
│   ├── stats.py                 # Statystyki i XP
│   ├── extra.py                 # Ekstra komendy
│   ├── welcome.py               # Powitania/Pożegnania
│   ├── tickets.py               # System ticketów
│   └── moderation.py            # Ban, kick, warn, clear
├── requirements.txt             # Zależności
├── .env.example                 # Template zmiennych
├── Procfile                     # Dla Render
└── README.md                    # Ten plik
```

## Dodawanie nowych komend

Tworz nowe pliki w folderze `cogs/` i implementuj komendę jako Cog.

Wszystkie komendy powinny używać `@app_commands.command()` zamiast `@commands.command()`.

## Funkcje

✅ **35+ slash komend**
✅ **System ticketów** - użytkownicy mogą tworzyć tickety  
✅ **Zarządzanie rolami** - admini mogą zarządzać rolami użytkowników
✅ **Statystyki & XP** - leaderboard, profile, ranking
✅ **Zabawy & Gry** - 8ball, kostki, monety, kawały
✅ **Powitania/Pożegnania** - automatyczne wiadomości
✅ **Moderacja** - ban, kick, warn, clear, slowmode
✅ **Informacje** - detale o serwerze, użytkownikach, bocie

## Wymagania

- Python 3.8+
- discord.py 2.4.0+
- python-dotenv
