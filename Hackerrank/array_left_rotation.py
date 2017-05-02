'''
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if left rotations are performed on array , then the array would become .

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.

Author: Mohsina Zaman
'''

def main():
	length, num = raw_input().split()
	length = int(length)
	num = int(num)
	s = raw_input()
	in_arr = map(int, s.split())
	#num = int(raw_input("Enter number of rotations"))
	new_list = []
	for i in range(len(in_arr)):
		new_list.append(in_arr[i])
	#print new_list

	for i in range(len(in_arr)):
		index = i-num
		#print "i is ", i
		#print "i-num is ",index
		#print "val at i "+str(i)+" is", in_arr[i]
		new_list[index] = in_arr[i]

	for i in range(len(new_list)):
		print str(new_list[i]),
	

main()
