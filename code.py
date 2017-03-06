import re
f1 = open("gerrit_repo.txt","r")
f2 = open("reolication_conf.txt","r")

l1 = []
for line in f1.readlines():
	tmp = line.split()
	l1.append(tmp)

l2 = []
for ele in l1:
	for val in ele:
		s = val.strip(".git")
		l2.append(s)
print l2
for line in f2.readlines():			
	#print line
	pattern = r"^\[(.*)\]"
        tmp1= re.match(pattern,line)
	if tmp1:
		#print tmp1.group(1).b(" ")[1][1:-1]
		if  tmp1.group(1).split(" ")[1][1:-1] in l2 :
			print "Available : " + tmp1.group(1).split(" ")[1][1:-1]
  		else:
			print "Not available : " + tmp1.group(1).split(" ")[1][1:-1]
        
             

