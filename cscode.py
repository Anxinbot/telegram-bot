import telegram

# 替换为实际的 token
bot = telegram.Bot(token='text1')
# 发送简单文本消息
bot.send_message(chat_id='text2', text="text3")
# 发送带标题网址链接
bot.send_message(chat_id='@XXXXXX', text='<a href="http://slowread.net/monitor-hostloc/">HOSTLOC 交易贴提醒</a>.', parse_mode=telegram.ParseMode.HTML)
# 复杂的文字样式
bot.send_message(chat_id=chat_id, text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', parse_mode=telegram.ParseMode.HTML)
# 发送图片
bot.send_photo(chat_id=chat_id,photo='<https://telegram.org/img/t_logo.png')
