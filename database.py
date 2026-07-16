import json
import os
from datetime import datetime


FILE = "bans.json"


def load_bans():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)



def save_bans(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)



def add_ban(userid, reason, moderator):

    bans = load_bans()

    bans[str(userid)] = {
        "reason": reason,
        "moderator": moderator,
        "date": str(datetime.now())
    }

    save_bans(bans)



def remove_ban(userid):

    bans = load_bans()

    if str(userid) in bans:
        del bans[str(userid)]

    save_bans(bans)



def is_banned(userid):

    bans = load_bans()

    return bans.get(str(userid))
