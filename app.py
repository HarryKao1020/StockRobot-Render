from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from dotenv import load_dotenv
import os;
import getStockInfo

# 載入 .env 文件中的環境變數
load_dotenv()

app = Flask(__name__)
# 設定成dev模式
app.config['FLASK_ENV'] = 'development'

# 讀取環境變數中的敏感資訊
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET')

# 如果是None 跳出錯誤訊息
if CHANNEL_ACCESS_TOKEN is None or CHANNEL_SECRET is None:
    raise ValueError("Missing LINE API credentials. Make sure CHANNEL_ACCESS_TOKEN and CHANNEL_SECRET are set.")

# 設置你的 Line Bot 的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# 自己的userId / 未來開放就要拿掉
user_id='U2032ae75254e026706d91546f58b9af1'
line_bot_api.push_message(user_id, TextSendMessage(text='你好，我是股市小幫手'))


@app.route("/callback", methods=['POST'])
def callback():
    # 獲取 Line 傳遞過來的 HTTP 請求頭部資訊
    signature = request.headers['X-Line-Signature']

    # 取得 HTTP 請求內容
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        # 驗證 HTTP 請求的簽名是否正確
        handler.handle(body, signature)
    except InvalidSignatureError:
        # 簽名錯誤時，拒絕此次請求
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    message=event.message.text

    if message =="查詢恐慌指數" :
        fear_index= getStockInfo.getFearIndex()
        maintenanceMargin = getStockInfo.getMaintenanceMargin()
        stock_info_data={**fear_index,**maintenanceMargin}
        message_text = """
            Fear Index: {},
            Fear Index Status: {},
            大盤融資維持率:{}
        """
        replyMessage = message_text.format(stock_info_data["Fear Index"],stock_info_data["Fear Index Status"],stock_info_data["大盤融資維持率"])
    else:
        replyMessage="查詢不到"

    # 當收到文字訊息時回覆replyMessage
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=replyMessage)
    )

if __name__ == "__main__":
    
    # == 本地用ngrok測試====
    app.run(host='0.0.0.0' ,port=5000)
