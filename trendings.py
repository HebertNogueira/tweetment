from tweepy_auth import TweepyAuth as ta
from connect_mongo import ConnectMongo as cm
from collection_rename import CollectionRename as cr
from datetime import datetime
import tweepy
import json
import sys
import time

class Trendings:

	def trendingCheck(now):
		
		# Autenticando no Twitter com Tweepy
		auth = ta.tweepyAuth()

		# Autenticando API
		api = tweepy.API(auth)

		# Configurando conexao do MongoDB
		client = cm.connectMongo()
		db = client.trendings

		# Renomeando BD Antigo
		cr.collectionRename(db,'trendingTopics',now)

		# Requisitando e salvando trending topics
		# BRAZIL = 23424768
		# WORLD = 1
		trends = api.trends_place(23424768)
		trends_result = json.loads(json.dumps(trends, indent=1))
		
		# Variaveis para iteracao
		result={}
		count = 48

		# Iterando para insercao no banco ...
		for trend_insert in trends_result:
			db.trendingTopics.insert_one(trend_insert)

		return (True)

	#Listando #1
	def listTrending():
		client = cm.connectMongo()
		db = client.trendings
		count = 0
		result={}
		for trend_return in db.trendingTopics.find():
			if count < 1:
				result[count] = trend_return['trends'][count]['name'].strip('#')
				print(result[count])
				count+=1
		return result[0]

	#Salvando polaridade no db
	def updateTrending(now,trending,polarity):
		client = cm.connectMongo()
		db = client.trendingsDisplay

		# Renomeando BD Antigo
		cr.collectionRename(db,'trendingTopicsDisplay',now)

		response = db.trendingTopicsDisplay.insert_one({'date':now,'tt':trending,'polarity':str(polarity)})
		return response