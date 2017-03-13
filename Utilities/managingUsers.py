#Author : Hena Firdaus
#13th March 2017 4 pm
#To Create clean dictionary
import json

users = json.loads(open("Users/Users.txt",'r').read())
ranks = json.loads(open("Users/Ranking.txt",'r').read())

dict1 ={}
rankDict = {}

f1 = open("Users/UserDict1.txt",'w')
f2 = open("Users/RankDict1.txt",'w')

cnt = 1

for handle in users:
	S = {}
	S["rating"] = str(users[handle])
	S["rank"] = str(ranks[handle])
    
	dict1[str(handle)] = S
	rankDict[str(ranks[handle])] = str(handle)

	cnt += 1

f1.write(str(dict1))
f2.write(str(rankDict))


