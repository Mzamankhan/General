

'''
def find_count(small,big):
	#print 'small is ',small
	#print 'big is ',big
	c = 0
	for s in small:
		#print 's is',s
		#print big.find(s)
		if big.find(s) <0:
			#print 'false'
			c+=2
	return c


def check_anagram():

	a = raw_input()
	b = raw_input()
	count = 0
	#check if two strings are the same
	if a == b:
		#print 'equal'
		return 0
	else: #strings are different
	#check if length is different
		#print 'not equal'
		if len(a) != len(b):
			count += abs(len(a)-len(b))
		if len(a)<len(b):
			count += find_count(a,b)
		else:
			count+= find_count(b,a)
		return count

'''
	

alph1 = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
alph2 = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
a = raw_input()
b = raw_input()

for s in a:
	alph1[s]+=1
for s in b:
	alph2[s]+=1

count = 0

for i in alph1:
	if alph1[i] != alph2[i]:
		diff = abs(alph1[i]-alph2[i])
		count += diff

print count