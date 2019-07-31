import sys

# Renomeando Colletion 

class CollectionRename():
	def collectionRename(db,collection,now):
		count = 0
		check = False
		for args in sys.argv:
			if (len(sys.argv) > 1):
				if (args == 'new' or args == 'ignite.py'):
					check = True
		
			if (check == True) or (count >= 1):
				check = False
			else:
				print ('Collection Rename: ' + collection)
				db[collection].rename(now)
				count+=1 