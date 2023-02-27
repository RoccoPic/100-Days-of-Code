import pandas

NATO_CSV = pandas.read_csv("nato_phonetic_alphabet.csv")

NATO_data_frame = pandas.DataFrame(NATO_CSV)
#print(NATO_data_frame)
#create a dictionary in this format

NATO_dict = {row.letter:row.code for (index,row) in NATO_data_frame.iterrows()}

#print(NATO_dict)

#create a list of phonetic words baed on the text the user inputs
is_on = True
while is_on:
    try:
        name = input("Enter a word: ")
        NATO_name = [NATO_dict[letter.upper()] for letter in name]
    except KeyError:
        print("Sorry,only leters in the alphabet please")
    else:
        print(NATO_name)
        is_on = False