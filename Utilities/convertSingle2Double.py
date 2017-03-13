#Author : Hena Firdaus
#13th March 2017 7:30 pm
#To convert single quotes to double quotes in json objects
import ast
import json

f = open('Users/UserDict.txt','r')
content = f.read()

#content = '"'+content+'"'
#print "Before :"
#print content

#content.replace("'",'"')
#content.replace('u"','')
content = ast.literal_eval(content)

#print "After :"
#print (json.dumps(content))

f1 = open('Users/UserDict.txt','w')
f1.write(str(json.dumps(content)))
