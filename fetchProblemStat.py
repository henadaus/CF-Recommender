#Author : Hena Firdaus
#15th March 2017 
#To fetch problem statistics
import urllib2
import json
import os

if os.path.exists("ProblemStatistics"):
	print "Folder 'ProblemStatistics' exists!!"
else:
	os.makedirs("ProblemStatistics")

url = 'http://codeforces.com/api/problemset.problems'

response = urllib2.urlopen(url).read()
res = json.loads(response)

result = res['result']['problemStatistics']

dict = {}
f  = open("ProblemStatistics/Statistics.txt",'w')

cnt = 1

for a in result:
	s = str(a['contestId'])+''+str(a['index'])
	dict[str(s)] = str(a["solvedCount"])
	print cnt
	cnt += 1

f.write(str(dict))
