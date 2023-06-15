import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_dict)


def generate_phoentic():
    entered_word = input("Enter a word: ").upper()
    try:
        code_word = [nato_dict[letter] for letter in entered_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phoentic()
    else:
        print(code_word)


generate_phoentic()
