#To download user's information i.e rating and rank
import mechanize
import re
import os
from bs4 import BeautifulSoup

br = mechanize.Browser()

prx = open("proxy" , 'r')
prx_set = prx.readline()
prx_set = prx_set.split('\n' , 1)
prx_set = prx_set[0]

if(len(prx_set) != 0):
	print prx_set
	br.set_proxies({"http":prx_set})

br.set_handle_robots(False)
br.addheaders=[('User-agent','Chromium')]

if(os.path.exists('Users')):
	print "User folder exists"
else:
	os.makedirs('Users');

#f = open('Users/User1.txt','w')
#f1 = open('Users/Ratings.txt','w')
f2 = open('Users/Ranking.txt','w')

#f.write("{\n")
#f1.write("{\n")
f2.write("{\n")

c = 0
rank = 0

for j in range(1,168):
	url = "http://codeforces.com/ratings/page/"+str(j)+""
	print str(j)+" completed"
	response = br.open(url)
	soup = BeautifulSoup(response)

	div = soup.find("div" , "datatable ratingsDatatable")

	table = div.find("table" , "")

	


	#print table
	rows = list()
	i = 0;
	for row in table.findAll("tr"):
		if(i != 0):
			#print row
			j = 0;
			for col in row.findAll("td"):
				if(j == 1):
					userI = col.find("a");
					user = userI['href']
					
				if(j == 3):
					rating = col
					
					rating = str(rating).replace("<td>", "")
					rating = str(rating).replace("</td>", "")
					rating = rating.strip()
					
				j += 1
			#print j
			#s = "{ user : "+str(user)+" , rating : "+str(rating)+"}\n"

			#s = "	\""+str(user[9:])+"\"\t\t\t:\t\""+str(rating)+"\" "
			#if(c != 33213):
			#	s = s + ","
			#s = s + "\n"
			#f.write(s);

			s = "	\""+str(user[9:])+"\"\t\t\t:\t \""+str(rank)+"\" "
			if(rank != 33213):
				s = s + ","
			s = s + "\n"
			f2.write(s);

			#s = "	\""+str(rank)+"\"\t\t\t:\t \""+str(rating)+"\" "
			#if(rank != 33213):
			#	s = s + ","
			#s = s + "\n"
			#f1.write(s);

		i += 1
		rank += 1
	c += 1	
	
	    
#f.write("}\n")
#f1.write("}\n")
f2.write("}\n")


		



