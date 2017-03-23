#Author : Hena Firdaus
#13th March 2017 3 pm
#To fetch submissions of user
import json
import urllib2
import httplib
import os

prx = open("proxy" , 'r')
proxy = prx.readline()
proxy = proxy.split('\n' , 1)
proxy = proxy[0]



if(len(proxy) != 0):
    print proxy
    proxy = urllib2.ProxyHandler({'http' : proxy })
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

if os.path.exists("Submissions"):
    print " 'Submission' directory exists !!"
else:
    os.makedirs("Submissions")

users = json.loads(open('Users/Users.txt').read())

f1 = open("Submissions/Submission.txt",'w')
f2 = open("Submissions/ErrorInDo.txt","w")

f1.write("{\n");
dict = {}
cnt = 1
for handle in users:
    print "Fetching submisisons of the user : "+handle+" Number :"+str(cnt)
    cnt += 1

    url = 'http://codeforces.com/api/user.status?handle='+handle
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    req = urllib2.Request(url, headers=hdr)
    
    try: 
        response = urllib2.urlopen(req).read()

        submission = json.loads(response)

        S = {}

        if submission["status"] == "OK":
            for sub in submission['result']:
                if sub['verdict'] == "OK":
                    s = str(sub['problem']['contestId'])+str(sub['problem']['index'])
                    S[s] = 1
            
            f1.write(" \""+str(handle)+' \" : '+str(S)+" , \n")
            #dict[str(handle)] = S
    
    except urllib2.HTTPError, e:
    	print "HTTPError = " + str(e.code)
    	f2.write(str(handle)+"\n")
        
    except urllib2.URLError, e:
    	print 'URLError = ' + str(e.reason)
    	f2.write(str(handle)+"\n")
        
    except httplib.HTTPException, e:
    	print 'HTTPException'
    	f2.write(str(handle)+"\n")
        
    
    

f1.write("}\n")   
#f1.write(str(dict))
