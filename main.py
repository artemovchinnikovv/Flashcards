import pandas as pd

data = pd.read_excel('data.ods')
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
