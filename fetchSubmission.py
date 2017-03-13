#Author : Hena Firdaus
#13th March 2017 3 pm
#To fetch submissions of user
import json
import urllib2
import os

if os.path.exists("Submissions"):
	print " 'Submission' directory exists !!"
else:
	os.makedirs("Submissions")

users = json.loads(open('Users/Users.txt').read())

f1 = open("Submissions/Submission.txt",'w')

dict = {}
cnt = 1
for handle in users:
	print "Fetching submisisons of the user : "+handle+" Number :"+str(cnt)
	cnt += 1

	url = 'http://codeforces.com/api/user.status?handle='+handle
	response = urllib2.urlopen(url).read()

	submission = json.loads(response)

	S = {}

	if submission["status"] == "OK":
		for sub in submission['result']:
			if sub['verdict'] == "OK":
				s = str(sub['problem']['contestId'])+str(sub['problem']['index'])
		        S[s] = 1
		
        dict[str(handle)] = S
        
    
f1.write(str(dict))