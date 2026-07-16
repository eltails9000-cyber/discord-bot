import json
import os
from datetime import datetime


FILE="data/bans.json"



def load():

    if not os.path.exists(FILE):
        return {}

    with open(FILE,"r") as f:
        return json.load(f)




def save(data):

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(FILE,"w") as f:
        json.dump(
            data,
            f,
            indent=4
        )




def ban(userid,reason,staff):

    data=load()


    data[str(userid)]={

        "userid":userid,
        "reason":reason,
        "staff":staff,
        "time":str(datetime.now()),
        "active":True

    }


    save(data)




def check(userid):

    data=load()

    return data.get(
        str(userid)
    )




def unban(userid):

    data=load()


    if str(userid) in data:

        del data[str(userid)]


    save(data)
