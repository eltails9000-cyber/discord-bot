from flask import Flask, request, jsonify
from database import add_ban, remove_ban
from roblox import send_message


app = Flask(__name__)



@app.route("/")
def home():

    return "Glory or death API Online"



@app.route("/ban", methods=["POST"])
def ban():

    data=request.json


    userid=data["userid"]
    reason=data["reason"]


    add_ban(
        userid,
        reason,
        "Discord"
    )


    send_message(
        f"BAN:{userid}"
    )


    return jsonify({
        "success":True
    })



@app.route("/unban", methods=["POST"])
def unban():

    data=request.json

    remove_ban(
        data["userid"]
    )


    return jsonify({
        "success":True
    })



app.run(
    host="0.0.0.0",
    port=8080
)
