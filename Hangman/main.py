from random_word import RandomWords
import os

word = RandomWords().get_random_word()
guess = ["_"]*len(word)
false = []


def draw(false):
    try:
        with open(f'drawings/{false}.txt', 'r') as file:
            drawing = file.read()
    except FileNotFoundError:
        drawing = """    
                           
                           
                           
                           
                       """
    return drawing


for _ in range(100):
    os.system("clear")
    print(f'{" ".join(guess)}                     uncorrect letters: {false}')
    print(draw(len(false)))
    if word == "".join(guess):
        print("Congrats! You win 🎉")
        exit()
    if len(false) == 9:
        break
    letter = input("Enter a letter: ")
    IN = False
    for index, value in enumerate(word):
        if letter == value:
            guess[index] = letter
            IN = True
    if IN is False and letter not in false:
        false.append(letter)
print("You lose! The word was", word)
