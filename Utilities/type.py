#Author : Hena Firdaus
#15th March 2017
#Storing the type of contests
import json

contest = json.loads(open("Contests/CF.txt","r").read())
gym = json.loads(open("Contests/Gym.txt","r").read())
f = open("Contests/Contest.txt",'w')

dict = {}
for a in contest['result']:
	s = a['id']
	d = {}
	d['type'] = str(a['type'])
	d['flag'] = 1
	dict[str(s)] = d


for a in gym['result']:
	s = a['id']
	d = {}
	d['type'] = str(a['type'])
	d['flag'] = 2
	dict[str(s)] = d
	
f.write(str(dict))
