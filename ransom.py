'''
A kidnapper wrote a ransom note but is worried it will be traced back to him.
 He found a magazine and wants to know if he can cut out whole words from it and use them to create an 
 untraceable replica of his ransom note. The words in his note are case-sensitive and he must use 
 whole words available in the magazine, meaning he cannot use substrings or concatenation to create 
 the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate 
his ransom note exactly using whole words from the magazine; otherwise, print No.
'''
'''
#Naive Approach : Search the magazine
def ransom_note(magazine, ransom):
    # if number of words in magazine less, then no need to check mor
    if(len(magazine)<len(ransom)):
    	return False
    else:
    	for word in ransom:
    		if word in magazine:
    			magazine.remove(word)
    			continue
    		else:
    			return False
    	return True
    			
'''


'''
#Hashmap approach
#Create dictionaries, then check for frequency
'''
def create_dict(l):
	new_dict = {}
	for word in l:
		if word in new_dict:
			new_dict[word]+=1
		else:
			new_dict[word] = 1
	return new_dict



def ransom_note(mag_dict, ran_dict):
	for ran_word in ran_dict:
		if ran_word in mag_dict: #if word exists in magazine
			#check frequency
			if mag_dict[ran_word] < ran_dict[ran_word]:
				return False
			else:
				continue
		else:  #word does not exist in magazine
			return False
	return True





m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
mag_dict = create_dict(magazine)
ran_dict = create_dict(ransom)
print mag_dict

answer = ransom_note(mag_dict, ran_dict)
if(answer):
    print "Yes"
else:
    print "No"
