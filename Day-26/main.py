import pandas
data = pandas.read_csv("Day-26/nato_phonetic_alphabet.csv")

phonetic_alpha_dict = {row.letter:row.code for index, row in data.iterrows()}
print(phonetic_alpha_dict)

user_word = input("Enter a word: ").upper()
word_letters = [phonetic_alpha_dict[letter] for letter in user_word]
print(word_letters)