#!/usr/bin/env python
import newspaper
import telegram
from kyotocabinet import *

bot = telegram.Bot('TOKEN')
db = DB()
db.open("users.kch", DB.OREADER)

def main():

	flipboard = newspaper.build(u'https://flipboard.com/@flipboarditalia/edizione-del-giorno-ts3tf1gpz', memoize_articles=False)
	i = 0
	for article in flipboard.articles:
		if i == 10:
			break
		article = flipboard.articles[i]
		article.download()
		article.parse()
		message = article.title + '\n\n' + article.url + '\n'

		cur = db.cursor()
		cur.jump()
		while True:
                    rec = cur.get(True)
                    if not rec: break
                    bot.sendMessage(rec[0].decode(encoding="utf-8", errors="strict"), message)
                    cur.disable()
		i += 1
		db.close()


if __name__ == '__main__':
    main()









