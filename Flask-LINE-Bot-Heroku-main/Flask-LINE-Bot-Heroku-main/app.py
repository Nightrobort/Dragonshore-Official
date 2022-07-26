import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"

StringforDevice = ""
StringforAction = ""
StringforBrand = ""
str1 = ""
number22 = 0

    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):


    get_message = event.message.text
    str1 = get_message.split("充電機")
    if len(str1) > 1:
        StringforDevice = "充電機"
    else :
        StringforDevice = ""
    str1 = ""
    str1 = get_message.split("買")
    if len(str1) > 1:
        StringforAction = "買"
    else :
        StringforAction = ""
    str1 = ""
    str1 = get_message.split("Mastervolt")
    if len(str1) > 1:
        StringforBrand = "Mastervolt"
    else :
        StringforBrand = ""
    str1 = ""


    
    
    # Send To Line
    reply = TextSendMessage("所以您是想" + StringforAction + StringforBrand + "的" + StringforDevice + "是嗎?")
    # reply = TextSendMessage(text=f"{get_message}")  原版 : 讀取訊息後回復一樣的訊息
    line_bot_api.reply_message(event.reply_token, reply)


