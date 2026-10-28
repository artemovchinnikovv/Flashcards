import pandas as pd
import random

class NotEnoughMistakenWords(Exception):
    pass

def random_def_ans_mist(n):
    data = pd.read_excel('words.ods')
    answer = data["Word"].tolist()
    definition = data["Definition"].tolist()
    frequency = data["Frequency"].tolist()
    answer_mist = []
    definition_mist = []
    frequency_mist = []
    for _ in range(len(answer)):
        if frequency[_]!=1:
            answer_mist.append(answer[_])
            definition_mist.append(definition[_])
            frequency_mist.append(frequency[_])
    answer = answer_mist
    definition = definition_mist
    frequency = frequency_mist
    if len(answer)<n:
        raise NotEnoughMistakenWords()
    r_int = [random.randint(1,(sum (frequency))) for _ in range (n)]
    r_int.sort()
    s = 0
    index = []
    for _ in range(len (answer)):
        s += frequency[_]
        if r_int[0]<=s:
            r_int = r_int[1:]
            index.append(_)
            if r_int == []:
                break
    answer = [answer[_] for _ in index]
    definition = [definition[_] for _ in index]

    return definition, answer

if __name__ == "__main__":
    print("Test")
    print(random_def_ans_mist(5))