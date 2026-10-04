import pandas as pd
import random

def random_def_ans(n):
    data = pd.read_excel('words.ods')
    answer = data["Word"].tolist()
    definition = data["Definition"].tolist()
    index = [random.randint(0,len (answer)) for _ in range (n)]
    answer = [answer[_] for _ in index]
    definition = [definition[_] for _ in index]

    return definition, answer
