#!/usr/bin/env python
import newspaper
import telegram

bot = telegram.Bot('TOKEN')

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
		bot.sendMessage('chat_id', message)
		i += 1



if __name__ == '__main__':
    main()









