import json
import neighbour
import fetchSolvedCount

def recommend(handle):
    neighbours = neighbour.getNeighbours(handle)

    totalSimilarity = 0

    for a in neighbours:
        totalSimilarity += a[0]

    submission = json.loads(open('Submissions/Submission.txt','r').read())
    CFStat = json.loads(open("ProblemStatistics/CFRound.txt",'r').read())
    GymStat = json.loads(open("ProblemStatistics/Gym.txt",'r').read())

    sub1 = submission[str(handle)+" "]

    print "Submission of user :"
    f1 = open("THisUser.txt",'w')

    for sub in sub1:
    	f1.write(str(sub))
    	f1.write("\n")


    question = {}
    finalQues = []

    for a in neighbours:
        handle2 = a[1]
        sub2 = submission[str(handle2)+" "]

        for sub in sub2:
            if sub not in sub1:
                question[sub] = 1

    print "Total questions : "+str(len(question))

    i = 1
    for ques in question:
        sum = 0
        for a in neighbours:
            handle2 = a[1]
            sub2 = submission[str(handle2)+" "]

            if ques in sub2:
                sum += a[0]

        try:
            if ques in CFStat:
        	    solvedCnt = int(CFStat[str(ques)])
            else:
        	    solvedCnt = int(GymStat[str(ques)])
            print "In recommendation :"+str(solvedCnt)

        
            if solvedCnt == 0:
                solvedCnt = 1

            p = sum/(totalSimilarity*solvedCnt)

            finalQues.append([p,ques])
            print i
            i += 1
        except:
            print str(ques)+" not found"
    finalQues.sort(lambda x,y: cmp(x[0],y[0]) , reverse = True)

    f = open("RecList.txt",'w')

    for a in finalQues:
        f.write(str(a[0])+" "+str(a[1]))
        f.write("\n")


if __name__ == "__main__":
	handle = raw_input("Enter handle :")
	recommend(handle)