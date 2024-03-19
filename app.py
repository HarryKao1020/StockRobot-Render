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

import os 
import json
import getStockInfo

app = Flask(__name__)

# 設置你的 Line Bot 的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('gIS4eSAOyETZv18tiyNcT4ZZ6274L9UuhLjSowpDjuqYf4dFCNB37+saXJfI1FSr85uiKqqrhteAxVCD3Yjalx/4zC3rshDGfm1/xZXIZmf4pFY2HYnRLs3LqbNiJAmBXAIOwCqSEZTqqnzNa8mfkwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('04279870980e7421fbf1b27cc03165c2')

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

    # 當收到文字訊息時回覆相同的訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=replyMessage)
    )

if __name__ == "__main__":
    
    # == 本地用ngrok測試====
    # app.run(port=5000)


    # 上到Render
    app.run(debug=True)