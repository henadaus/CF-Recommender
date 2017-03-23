#To fetch SolvedCount of problems of Gyms
import os
import json
import urllib2
from bs4 import BeautifulSoup
import httplib

url = 'http://codeforces.com/api/contest.list?gym=true'

prx = open("proxy" , 'r')
proxy = prx.readline()
proxy = proxy.split('\n' , 1)
proxy = proxy[0]



if(len(proxy) != 0):
    print proxy
    proxy = urllib2.ProxyHandler({'http' : proxy })
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

if os.path.exists('ProblemStatistics'):
    print "The directory 'ProblemStatistics' exists !!!"
else:
    os.makedirs('ProblemStatistics')

dict = {}
f1 = open("ProblemStatistics/Gym.txt","w")
f2 = open("ProblemStatistics/Errors.txt","w")

response = urllib2.urlopen(url).read()
res = json.loads(response)

result = res['result']
cnt = 1
for a in result:
    contestId = a['id']
    url = 'http://codeforces.com/gym/'+str(contestId)
    
    cnt += 1
    print " Number : "+str(cnt)+" "+url

    try:
        response = urllib2.urlopen(url).read()
        #f = open("Src.txt",'r').read()
        soup = BeautifulSoup(response)
        div = soup.find("div","datatable")
        table = div.find("table","problems")
     
        i = 0
        flag = 0

        for row in table.findAll("tr"):
            if i != 0:
                j = 1
                for col in row.findAll("td"):
                    if j == 1:
                        pid = col.find("a")
                        print "pid :"+str(pid.get_text())
                        pid = str(pid.get_text()).strip()
                        #if pid != index:
                        #   break
                    if j == 4:
                        solved = col.find("a")
                        #print "check : "+str(solved)
                        if str(solved) == "None":
                            solved = 0
                        else:
                            solved = solved.get_text().encode('utf-8')
                            solved = solved[3:]
                    
                        print "solved count :"+str(solved)
                    
                    j += 1
                problem = str(contestId)+str(pid)
                dict[problem] = solved
                print "Problem : "+problem+" solved : "+str(solved)
            i += 1
     
    except urllib2.HTTPError,e:
        f2.write(str(problem)+"\n")
        print "HTTPError = " + str(e.code)
        
        #checksLogger.error('HTTPError = ' + str(e.code))
    except urllib2.URLError, e:
        f2.write(str(problem)+"\n")
        print 'URLError = ' + str(e.reason)
        
        #checksLogger.error('URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
        f2.write(str(problem)+"\n")
        print 'HTTPException'
       
f1.write(str(dict))
