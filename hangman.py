import random

def display(secret,miss,found):
    print("\nTotal guessed:",len(miss)+len(found))
    print("Wrong Guesses:",len(miss))
    print("Missed letters:"," ".join(miss))
    print("Word:"," ".join([c if c in found else "_" for c in secret]))

def play():
    print("Welcome to Hangman!")
    print("🎮 A world of game 🕹️🕹️️")
    lst=["python","online","output","action","photos"]
    secret=random.choice(lst).upper()
    miss=[]
    found=[]
    guessed=0
    while len(miss)<=6:
        display(secret,miss,found)
        if all(c in found for c in secret):
            print("🤗 Congrats! you won 🫂")
            return
        while True:
            letter=input("Guess a letter:").upper()
            if len(letter)>1:
                print("😊 Enter single character\n")
            elif not letter.isalpha():
                print("😊 Enter a Letter\n")
            elif letter in found or letter in miss:
                print("You have already guessed it\n")
            else:
                break
        
        if letter in secret:
            found.append(letter)
        else:
            miss.append(letter)
    print(f"\nOops,you lost! the word was \'{secret}\'")
    if input("Do you want to play again(yes/no):").upper().startswith("Y"):
        print()
        play()

if __name__=="__main__":
    play()