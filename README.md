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

## Komendy - Pełna Lista (45+)

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

### 💰 Ekonomia
- `/balance [użytkownik]` - Sprawdź portfel 💵
- `/work` - Pracuj i zarabiaj (15-50 💵, cooldown 30m) 💼
- `/daily` - Bonus codzienny (100 💵, cooldown 24h) 🎁
- `/shop` - Pokaż sklep 🛒
- `/buy [item]` - Kup przedmiot (jabłko, burger, pizza, sushi, diament, złoto)
- `/inventory` - Pokaż swoje przedmioty 📦
- `/gamble [stawka]` - Graj w papier-kamień-nożyce 🎰
- `/transfer [użytkownik] [kwota]` - Prześlij pieniądze 💸

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

### 🎫 System Ticketów (Rozbudowany)
- `/create-ticket [typ] [powód]` - Stwórz ticket
  - **Typy ticketów:** 🐛 Bug Report, ✨ Feature Request, 🆘 Support/Pomoc
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

## Struktura projektu

```
.
├── main.py                      # Główny plik bota
├── config.py                    # Konfiguracja
├── cogs/                        # Folder z komendami
│   ├── info.py                  # Komendy help, info, ping
│   ├── slash_commands.py        # Dodatkowe komendy info
│   ├── fun.py                   # Zabawy (8ball, dice, coin, joke, rps)
│   ├── economy.py               # Ekonomia (10 komend)
│   ├── roles.py                 # Zarządzanie rolami
│   ├── stats.py                 # Statystyki i XP
│   ├── extra.py                 # Ekstra komendy
│   ├── welcome.py               # Powitania/Pożegnania
│   ├── tickets.py               # System ticketów (3 typy)
│   └── moderation.py            # Ban, kick, warn, clear, slowmode
├── requirements.txt             # Zależności
├── .env.example                 # Template zmiennych
├── Procfile                     # Dla Render
└── README.md                    # Ten plik
```

## Główne Funkcje

✅ **45+ slash komend** - pełny zestaw funkcji
✅ **Ekonomia** - zarabianie, sklep, przedmioty, transfer, gry o pieniądze
✅ **System ticketów z typami** - 3 rodzaje (Bug, Feature, Support)
✅ **Zarządzanie rolami** - admini mogą zarządzać rolami
✅ **Statystyki & XP** - leaderboard, profile, ranking
✅ **Zabawy & Gry** - 8ball, kostki, monety, kawały, papier-kamień-nożyce
✅ **Powitania/Pożegnania** - automatyczne wiadomości
✅ **Moderacja** - ban, kick, warn, clear, slowmode
✅ **Informacje** - detale o serwerze, użytkownikach, bocie

## System Ekonomii

**Zarabianie pieniędzy:**
- `/work` - Pracuj (15-50 💵, cooldown 30m)
- `/daily` - Bonus codzienny (100 💵, cooldown 24h)
- `/gamble [stawka]` - Graj w papier-kamień-nożyce

**Wydawanie pieniędzy:**
- `/shop` - Sklep z przedmiotami
- `/buy [item]` - Kupuj przedmioty (jabłko, burger, pizza, sushi, diament, złoto)
- `/transfer [użytkownik] [kwota]` - Prześlij pieniądze

**Sprawdzanie:**
- `/balance` - Sprawdź saldo
- `/inventory` - Sprawdź przedmioty

## Wymagania

- Python 3.8+
- discord.py 2.4.0+
- python-dotenv

## Status

✨ **v4.0** - Ekonomia + System ticketów z typami (45+ komend)

