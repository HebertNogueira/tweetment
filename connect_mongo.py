from pymongo import MongoClient

class ConnectMongo():
	def connectMongo():
		client = MongoClient('localhost', 27017)
		return client