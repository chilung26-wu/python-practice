from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage

channel_token  = "DJ3TA9xdjLjjXTO58wg4Uhr8HVdKo8ir3AXuzAAzOWD0uQMbtSOoaWfkHK4I1qVCKlY8VjBoQsz6P7BO5XFmn7nldSH0YZv6rfvZB8KEc9HaZLE6BvSa29nytZY96wnASR4jxbJmwhI5V6B4WEFMKQdB04t89/1O/w1cDnyilFU="
channel_secret = "b207158cf93496484a8201e76e38cdfc"

app = Flask(__name__)
line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(port=8080)