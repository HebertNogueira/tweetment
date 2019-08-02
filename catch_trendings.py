from textblob_trendings import TextblobTrendings as tb
from matplotlib_gauge import MatplotlibGauge as mg
from tweepy_auth import TweepyAuth as ta
from connect_mongo import ConnectMongo as cm
from collection_rename import CollectionRename as cr
import tweepy
import json
import threading
import time
import sys

class CatchTrendings():

	def catchTrendings(trendingLoad, now):

		# Autenticando no Twitter com Tweepy
		auth = ta.tweepyAuth()

		# Configurando streaming e salvamento no db
		class MyListener(tweepy.streaming.StreamListener):
			def on_data(self, dados):
				tweet = json.loads(dados)
				tweetText = {"text":tweet['text']}
				if (tweetText['text'][:2] != 'RT'):
					db.tweets.insert_one(tweetText)
					print (tweetText['text'])
				return True
		mylistener = MyListener()
		mystream = tweepy.Stream(auth, listener = mylistener)

		# Criando a conexão ao MongoDB
		client = cm.connectMongo()
		db = client.twitterCollection

		# pegando Trending #1
		trending = [str(trendingLoad)]


		def streamStart():
			# Abrindo thread com o stop do Streaming
			threading.Thread(target=catchTweet).start()
			
			#Iniciando o streaming de tweets
			mystream.filter(track=trending)
			
			# Executando a analise de sentimentos (Apos stop do streaming)
			textblob = tb.sentimentCheck(now,trendingLoad)

			#Gerando imagem do gauge
			mg.gauge(polarity=textblob, tweetWord=str(trendingLoad))

			# Renomeando collection com tweets salvos para backup 
			db = client.twitterCollection
			cr.collectionRename(db,'tweets',now)

			# Renomeando collection com TT salvos para backup
			db = client.trendings
			cr.collectionRename(db,'trendingTopics',now)

		# metodo para executar em thread e efetuar stop do streaming
		def catchTweet():

			howmuch = 200
			count = 0
			for args in sys.argv:
				if (args != 'ignite.py'):
					if (args != 'new'):
						try:
							howmuch = int(args)
						except:
							pass

			tweet_list = {}
			keepGoing = True
			while (keepGoing == True):
				if (len(tweet_list) > howmuch):
					mystream.disconnect()
					keepGoing = False
				else:
					time.sleep(1)
					#aguarda 1 segundo e refaz a consulta
					count=0
					tweets = []
					for tweet in db.tweets.find():
						tweet_list[count] = tweet['text']
						count+=1
					print('========> ' + str(len(tweet_list)))

		# Thread inicial!
		threading.Thread(target=streamStart).start()

