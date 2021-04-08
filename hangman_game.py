import random
import os

def read_file():
    with open("./files/data.txt",'r', encoding="utf-8") as f:
        data_list = [word.strip() for word in f]
        return data_list

def get_word():
    word = random.choice(read_file())
    return word

def remove_accents(word):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b)
    return word

def main():

    word = get_word()
    word_normalize = word.lower()
    word_normalize = remove_accents(word_normalize)
    guess = ["_"] * len(word)


    while "".join(guess) != word:
        #Clean the terminal
        os.system("cls")

        # Print text
        print("¡Adivina la palabra!")
        print(f'{" ".join(guess).capitalize()}')


        # input
        letter = input("Ingresa una letra: ")
        letter = letter.lower()
        letter = remove_accents(letter)

        #Changing the correct letters
        if letter in word_normalize:
            index = tuple(idx for idx, x in enumerate(word_normalize) if x==letter)
            for i in index:
                guess[i] = word[i]

    os.system("cls")

    #Win
    print(f"Ganaste la palabra era: {word.capitalize()}")


if __name__ == '__main__':
    main() 