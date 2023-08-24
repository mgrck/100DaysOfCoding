import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = (input("Enter a word: ")).upper()
    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in thr alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()