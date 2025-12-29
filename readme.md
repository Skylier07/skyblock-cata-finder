# Hypixel SkyBlock Catacombs Level Helper

<a href="https://github.com/Skylier07/skyblock-cata-finder">
  <img alt="GitHub last commit (branch)"
       src="https://img.shields.io/github/last-commit/Skylier07/skyblock-cata-finder/main">
</a>

A simple Python helper utility to fetch a **Hypixel SkyBlock player’s Catacombs level** using their Minecraft username.

This script uses the **Mojang API** to resolve usernames to UUIDs and the **Hypixel API** to retrieve SkyBlock profile data and dungeon experience.

---

## Features

- Get a player’s **UUID** from their Minecraft username
- Fetch all SkyBlock profiles for a player
- Extract **Catacombs XP** across profiles
- Calculate and return the **highest Catacombs level**
- Lightweight and easy to integrate into other projects

---

## Requirements

- Python 3.7+
- `requests` library
- A valid **Hypixel API key**

Install dependencies:

```bash
pip install requests
```

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Skylier07/skyblock-cata-finder
cd get_dungeon
```

2. Create a `keys.py` file in the project root:

```python
API_KEY = "YOUR_HYPIXEL_API_KEY"
```

For more on Hypixel API keys, visit Hypixel's website: https://api.hypixel.net/

---

## Usage

### Get a player’s Catacombs level

```python
from your_file_name import get_level

level = get_level("PlayerUsername")
print(level)
```

### Available Helper Functions

- `get_uuid(username)`
  Returns the Minecraft UUID for a username

- `get_player_profiles(player_name=None, uuid=None)`
  Returns all SkyBlock profiles for a player

- `get_cata_xp(player_name)`
  Returns the highest Catacombs XP across profiles

- `get_level(player_name)`
  Returns the calculated Catacombs level

---

## How It Works

1. Converts the username into a UUID using the Mojang API
2. Fetches SkyBlock profiles from the Hypixel API
3. Collects Catacombs experience from each profile
4. Uses predefined XP thresholds to determine the Catacombs level

---

## Notes & Limitations

- If a player has **no Catacombs data**, the function may return `None`
- If the API key is expired or invalid, the script will fail
- Hypixel API rate limits apply
- Only supports **Catacombs levels up to 40**

---

## Disclaimer

This project is **not affiliated with Hypixel**.
All data is provided by the official Hypixel and Mojang APIs.

---

## License

MIT License — feel free to use, modify, and distribute.
