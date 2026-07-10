import pandas as pd

filename = input()

data = pd.read_excel(filename+'.ods')
word = data["Word"].tolist()
defin = data["Definition"].tolist()
freq = data["Frequency"].tolist()

def find_num(list, n):
	S = 0
	i = 0
	while n>S:
		S = S + list[i]
		i = i + 1
	return i

import random
for i in range(5):
	rand_num = random.randint(1, sum (freq))
	n = find_num(freq, rand_num) - 1
	print (defin[n])
	answer = input()
	if answer==word[n]:
		print ("You are right!")
		if freq[n]>1:
			freq[n] = freq[n] // 2
	else:
	    print ("Wrong, but you can try again")
	    answer = input()
	    if answer==word[n]:
	        print ("You are right!")
	    else:
	        print ("Wrong, the answer is "+word[n])
	        freq[n] = freq[n]*2
data["Frequency"] = freq
data.to_excel((filename+'.ods'), index=False)
