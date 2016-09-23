#!/usr/bin/env python
import newspaper
import telegram

bot = telegram.Bot('TOKEN')

def main():

	la_stampa_rss = newspaper.build(u'http://www.lastampa.it/rss.xml')
	i = 0
	for article in la_stampa_rss.articles:
		
		article = la_stampa_rss.articles[i]
		article.download()
		article.parse()
		message = article.title + '\n\n' + article.url + '\n'
		bot.sendMessage('chat_id', message)
		i += 1



if __name__ == '__main__':
    main()









