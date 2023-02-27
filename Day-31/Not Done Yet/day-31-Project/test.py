import pandas
import random

word_list = pandas.read_csv("./data/french_words.csv")
to_learn = word_list.to_dict(orient="records")
current_card = random.choice(to_learn)
print(current_card)
print(len(to_learn))
to_learn.remove(current_card)
print(len(to_learn))



with open ("./data/the_words.csv","w") as known:
    for item in to_learn:
        known.write(f"{item['French']},{item['English']}\n")
