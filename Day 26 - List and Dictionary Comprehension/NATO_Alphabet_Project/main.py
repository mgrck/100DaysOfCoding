import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.

word = (input("Enter a word: ")).upper()

result = [phonetic_dict[letter] for letter in word]

print(result)