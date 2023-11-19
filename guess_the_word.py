import random
import os

def main():
    clear()
    corrects = []
    inp = ""
    word = word_selector()
    lines(word)
    guessed = 0
    while guessed != len(word):
        guess = guesss(word)
        guessed = guessed + guess[0]
        corrects.append(guess[1])
        letters(corrects)
        lines(word)
    
    while(inp != word):  
        if guessed == len(word):
            inp = input("Whats the word:")
            if inp != word:
                print("That's not correct")
    print("You win!")
    
def lines(word):    
    print("Guess the word:")
    for i in range (len(word)):
        print("_ ", end='')
    print('')
        
def letters(corrects):
    for i in range(len(corrects)):
        print(corrects[i], end=' ')
    print('')

def word_selector():
    words = ["cat", "dog", "dolphin"]
    random_number = random.randint(0, 2)
    return(words[random_number])

def guesss(correct):
    miss = True
    while(miss):
        inp = input()
        if not inp.isdigit():
            if len(inp)>1:
                print("Write only a single letter")
            if len(inp) == 1:
                break
    checked = check_letter(correct, inp)
    return [checked, inp]

def check_letter(correct, inp):
    if inp in correct:
        clear()
        return 1
    if inp not in correct:
        return 0

def clear():
    os.system('clear')

if __name__ == "__main__":
    main()
