import requests
import json
from keys import API_KEY

api_url = "https://api.hypixel.net/v2/resources/skyblock/"
CATACOMBS_XP = {
    15: 25340,
    16: 35640,
    17: 50040,
    18: 70040,
    19: 97640,
    20: 135640,
    21: 188140,
    22: 259640,
    23: 356640,
    24: 488640,
    25: 668640,
    26: 911640,
    27: 1239640,
    28: 1684640,
    29: 2284640,
    30: 3084640,
    31: 4149640,
    32: 5559640,
    33: 7459640,
    34: 9959640,
    35: 13259640,
    36: 17559640,
    37: 23159640,
    38: 30359640,
    39: 39559640,
    40: 51559640,
}


def get_uuid(username):
    resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    try:
        uuid = resp.json()["id"]
        return uuid
    except KeyError as e:
        return None

def get_player_profiles(player_name=None, uuid=None):
    url = f"https://api.hypixel.net/v2/skyblock/profiles?key={API_KEY}"
    if not player_name and not uuid:
        return None
    
    if not uuid:
        uuid = get_uuid(player_name)

    try:
        params = {"uuid": uuid}
        response = requests.get(url, params=params)

        response.raise_for_status()  
        profiles = response.json()["profiles"]
        return profiles
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something went wrong", err)

def get_cata_xp(player_name):
    uuid = get_uuid(player_name)
    profiles = get_player_profiles(uuid=uuid)
    xps=[]
    try:
        for profile in profiles:
            try: 
                xps.append(profile['members'][uuid]['dungeons']['dungeon_types']['catacombs']['experience'])
            except Exception as e:
                pass

        return max(xps)
    except Exception as e:
        print("API Key Expired")

def get_level(player_name):
    xp = get_cata_xp(player_name)

    level = 0
    for lvl, required_xp in sorted(CATACOMBS_XP.items()):
        if xp >= required_xp:
            level = lvl
        else:
            break
    return level