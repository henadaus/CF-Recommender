#Author : Hena Firdaus
#13th March 2017 

#To find similar neigbours
import json
import compare

def getNeighbours(handle):
	users = json.loads(open('Users/UserDict.txt','r').read())
	ranklist = json.loads(open('Users/RankDict.txt','r').read())

	rank = int(users[str(handle)]['rank'])
	print "Handle :"+handle+" Rank :"+str(rank)

	if rank-10 >= 1:
		up = rank - 10
	else:
		if rank == 1:
			up = 0
		else:
		    up = 1

	if rank+10 <= 50:
		down = rank + 10
	else:
		if rank == 50:
			down = 0
		else:
		    down = 50
    
	neighbours = []

	if up != 0:
		for i in range(up,rank):
			handle2 = ranklist[str(i)]
			print "Going(up) to  compare with : "+str(handle2)
			sim = compare.cosineSimilarity(handle,handle2)
			print "		Similarity : "+str(sim)
			l = [sim , str(handle2)]
			neighbours.append(l)

	if down != 0:
		for i in range(rank+1,down+1):
			handle2 = ranklist[str(i)]
			print "Going(down) to  compare with : "+str(handle2)
			sim = compare.cosineSimilarity(handle,handle2)
			print "		Similarity : "+str(sim)
			l = [sim , str(handle2)]
			neighbours.append(l)

	neighbours.sort(lambda x,y : cmp(x[0] , y[0]) , reverse = True)
	#print neighbours

	#Selecting top 10 neighbours
	finalNeigh = []
	counter = 1

	for n in neighbours:
		finalNeigh.append(n[1])
		counter += 1
		if counter == 11:
			break

	print finalNeigh




if __name__ == "__main__":
	handle = raw_input("Enter handle : ")
	getNeighbours(handle)