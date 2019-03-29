from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage

# init api
access_token = 'ENTER-CHANNEL-ACCESS-TOKEN'
line_bot_api = LineBotApi(access_token)

to = 'ENTER-USER-ID'

# send message
line_bot_api.push_message(to, (
    TextSendMessage(text='สวัสดีจ้า'),
    StickerSendMessage(package_id=11537, sticker_id=52002745)
))

# https://developers.line.biz/en/reference/messaging-api/#message-objects
# https://developers.line.biz/media/messaging-api/sticker_list.pdf
