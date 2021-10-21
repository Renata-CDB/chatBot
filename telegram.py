import telepot, json, time
from telepot.loop import MessageLoop

with open("token.json") as jsonFile:
  token = json.load(jsonFile)
bot = telepot.Bot(token)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10) 