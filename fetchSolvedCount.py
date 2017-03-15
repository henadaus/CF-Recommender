import json
import urllib2
from bs4 import BeautifulSoup

def getSolvedCnt(ques):
    c = 0
    for a in ques:
        if a >= 'A' and a <= 'Z':
            break
        else:
            c += 1

    contestId = ques[:c]
    index = ques[c:]

    print "Contest ID : "+contestId + " Index : "+index

    contestType = json.loads(open("Contests/Contest.txt").read())
    typeC = int(contestType[str(contestId)]['flag'])
    print typeC

    if typeC == 1:
        url = 'http://codeforces.com/contest/'+str(contestId)
    else:
        url = 'http://codeforces.com/gym/'+str(contestId)

    print url

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
                    if pid != index:
                        break
                if j == 4:
                    solved = col.find("a")
                    solved = solved.get_text().encode('utf-8')
                    solved = solved[3:]
                    print solved
                    print "solved count :"+solved
                    flag = 1
                j += 1
            if flag == 1:
                break;
        i += 1

    return int(solved)



if __name__ == "__main__":
    ques = raw_input("Enter question :")
    getSolvedCnt(ques)
