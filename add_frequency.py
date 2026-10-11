import pandas as pd
import random

def add_frequency(definition_chosed, mistakes):
    data = pd.read_excel('words.ods')
    definition = data["Definition"].tolist()
    frequency = data["Frequency"].tolist()
    for i in range(len (definition_chosed)):
        frequency[definition.index(definition_chosed[i])] *= (4 ** mistakes[i])
    data["Frequency"] = frequency
    data.to_excel(("words.ods"), index=False)