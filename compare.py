#Author : Hena Firdaus
#13th March 2017

import json
import math



def cosineSimilarity(handle1,handle2):
    submissions = json.loads(open("Submissions/Submission.txt",'r').read())
    #print submissions
    print "Hello"
    sub1 = submissions[str(handle1)]
    sub2 = submissions[str(handle2)]

    print "DOne"
    len1 = len(sub1)
    len2 = len(sub2)

    print "User 1 solved : "+str(len1)+" problems"

    print "User 2 solved : "+str(len2)+" problems"

    #print sub1
    if len1 < len2:
        a = sub1
        b = sub2
    else:
        a = sub2
        b = sub1

    cnt = 0

    for sub in a:
        if sub in b:
            cnt += 1

    print "The have solved "+str(cnt)+" same problems"

    cosSimilarity = cnt/(math.sqrt(len1) * math.sqrt(len2))

    return cosSimilarity

if __name__ == "__main__" :
    handle1 = raw_input("Enter user 1 :")
    handle2 = raw_input("Enter user 2 :")
    print cosineSimilarity(handle1,handle2)