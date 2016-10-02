import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from kyotocabinet import *

bot = telegram.Bot('TOKEN')
users = []

db = DB()

db.open("users.kch", DB.OWRITER | DB.OCREATE)

def main():

    update_id = 0

    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None

    while True :
            try:
                    update_id = create_database(bot, update_id)
            except NetworkError:
                    print("Network error!")
                    sleep(1)
            except Unauthorized:
                    print("Error: user unauthorized")
                    update_id += 1



def create_database(bot, update_id):
    log = open('log.txt', 'a')
    for update in bot.getUpdates(offset=update_id, timeout=10):
        chat_id = update.message.chat_id
        update_id = update.update_id+1
        message = update.message.text
        firstname = update.message.from_user.first_name
        lastname = update.message.from_user.last_name
        iduser = str(update.message.from_user.id)
        info = str(chat_id) + ' ' + firstname + ' ' + lastname

        if message == '/start':
            welcome_message(chat_id, firstname)
            log.write( info + ' started the bot\n')

        if message == '/subscribe':
            if chat_id not in users:
                users.append(chat_id)
                db.set(chat_id, None)
                log.write(info + ' subscribed\n')
                bot.sendMessage(chat_id, 'Successfully subscribed\n')
            else:
                bot.sendMessage(chat_id, 'Already subscribed!\n')
                log.write(info + 'has already subscribed\n')
        if message == '/unsubscribe':
            try:
                users.remove(chat_id)
                db.remove(chat_id)
                log.write(info + ' unsubscribed\n')
                bot.sendMessage(chat_id, 'Successfully unsubscribed\n')

            except:
                bot.sendMessage(chat_id, 'Not subscribed!\n')
                log.write(info + ' has already unsubscribed\n')
    db.close()
    log.close()
    return update_id

def welcome_message(chat_id, name):
	welcome = 'Welcome ' + name +'\nPrompt /subscribe to receive news daily\n'
	bot.sendMessage(chat_id, welcome)

if __name__ == '__main__':
    main()
