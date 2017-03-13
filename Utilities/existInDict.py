#To check if an element exists in a dictionary
import json

f = open("newCheck.txt",'r')

s = json.loads(f.read())

s1 = s[str('tourist')]
s2 = s[str('Petr')]

print json.dumps(s1)
print json.dumps(s2)

cnt = 0
print "Starting..."
for sub in s1:
	if sub in s2:
		cnt += 1
		print sub

print 'Same ppl are : '+str(cnt)