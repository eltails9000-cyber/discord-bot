import requests
from config import ROBLOX_API_KEY, UNIVERSE_ID



def send_ban(userid, reason):

    url = (
        f"https://apis.roblox.com/cloud/v2/universes/"
        f"{UNIVERSE_ID}/data-stores"
    )


    headers = {
        "x-api-key": ROBLOX_API_KEY
    }


    data = {
        "userid": userid,
        "reason": reason
    }


    r = requests.post(
        url,
        headers=headers,
        json=data
    )


    return r.status_code



def send_message(message):

    url = (
        f"https://apis.roblox.com/messaging-service/v1/"
        f"publish"
    )


    headers = {
        "x-api-key": ROBLOX_API_KEY
    }


    data = {
        "message": message
    }


    return requests.post(
        url,
        headers=headers,
        json=data
    )
