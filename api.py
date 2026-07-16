from flask import Flask, request, jsonify
import os

from database import add_ban, remove_ban
from roblox import send_message


app = Flask(__name__)


# =====================
# CONFIG
# =====================

API_KEY = os.getenv(
    "API_KEY"
)


# Cola de comandos para Roblox
commands = []


# =====================
# SECURITY
# =====================

def verify_key():

    key = request.headers.get(
        "x-api-key"
    )

    return key == API_KEY



# =====================
# HOME
# =====================

@app.route("/")
def home():

    return "Glory or Death API Online"



# =====================
# DISCORD -> ROBLOX BAN
# =====================

@app.route("/ban", methods=["POST"])
def ban():

    if not verify_key():
        return jsonify({
            "error":"Unauthorized"
        }),401


    data = request.json


    userid = str(data["userid"])
    reason = data.get(
        "reason",
        "No reason"
    )


    add_ban(
        userid,
        reason,
        "Discord"
    )


    commands.append({

        "action":"ban",
        "userid":userid,
        "reason":reason

    })


    send_message(
        f"BAN:{userid}"
    )


    return jsonify({

        "success":True,
        "message":"Ban added"

    })




# =====================
# DISCORD -> ROBLOX UNBAN
# =====================

@app.route("/unban", methods=["POST"])
def unban():

    if not verify_key():
        return jsonify({
            "error":"Unauthorized"
        }),401



    data=request.json


    userid=str(
        data["userid"]
    )


    remove_ban(
        userid
    )


    commands.append({

        "action":"unban",
        "userid":userid

    })


    return jsonify({

        "success":True,
        "message":"Unban added"

    })





# =====================
# ROBLOX CHECK COMMANDS
# =====================

@app.route("/commands")
def get_commands():


    if not verify_key():

        return jsonify({

            "error":"Unauthorized"

        }),401



    if len(commands) == 0:

        return jsonify({

            "action":"none"

        })



    return jsonify(
        commands.pop(0)
    )





# =====================
# RUN
# =====================

app.run(

    host="0.0.0.0",

    port=8080

)
