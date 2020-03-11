import platform
import random
import os 
import sys
import time
listofnumbers = []
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')

number = random.randint(1,100)

def type(string):
  for char in string:  
    sys.stdout.write(char)
    sys.stdout.flush() 
    time.sleep(0.06)

def start():
    clear()
    type("Welcome! \n")
    type("Do you want the rounds to be limited or to count you? Please print 1 for limited and 2 for unlimited rounds:  \n")
    option = input("")
    if option == '1':
        option1()
    elif option == '2':
        option2()


def option1():
    try:
        rounds = 10
        guesses = 1
        while rounds > 0:
            guess = input("Number ")
            if int(guess) in listofnumbers:
                print(listofnumbers)
                print("Already used number!")
                guess = input("Number ")
            elif int(guess) not in listofnumbers:
                listofnumbers.append(int(guess))
                if int(guess) == number:
                    print("Won")
                    if guesses == 1:
                        print("You did it in 1 round!")
                    else:
                        print("You did it in %s rounds" % guesses)
                    break
                elif int(guess) > number:
                    clear()
                    print("too high")
                    rounds -= 1
                    guesses += 1 
                    print("You have %s rounds left" % rounds)
                elif int(guess) < number:
                    clear()
                    print("Too low")
                    rounds -= 1
                    guesses += 1
                    print("You have %s rounds left" % rounds)
        print("Number to get was " + str(number))
        play_again = input("Play again? Y/N")
        if play_again.upper() == 'Y':
            start()
        elif play_again.upper() == "N":
            sys.exit()
        else:
            print("Please either do Y or N")
            play_again = input("Play again? Y/N")
    except ValueError:
        print("Sorry, you may only use numbers, no letters")
        time.sleep(2)
        clear()
        option1()

def option2():
    try:
        guesses = 0
        rounds = 1
        clear()
        while rounds == 0 or rounds > 0:
            print("Round %s" % str(rounds))
            guess = input("Number ")
            if int(guess) in listofnumbers:
                print("You have already used that number before")
                print(listofnumbers)
            elif int(guess) not in listofnumbers:
                listofnumbers.append(int(guess))
                if int(guess) > number:
                    clear()
                    print("Too high")
                    rounds += 1
                    guesses += 1
                elif int(guess) < number:
                    clear()
                    print("Too low")
                    rounds += 1
                    guesses += 1
                elif int(guess) == number:
                    clear()
                    print("You got it! It was " + str(number))
                    print("You did it in %s guesses" % guesses)
                    playagain = input("Do you wanna play again?")
                    if playagain.lower() == 'yes' or playagain.lower() == 'y':
                        clear()
                        start()
                    elif playagain.lower() == 'no' or playagain.lower() == 'n':
                        sys.exit()
                    else:
                        print("Please either do 'Y' or 'N'")
                        playagain = input("Do you want to play again?")
    except ValueError:
        print("Sorry, you may only use numbers, no letters")
        time.sleep(2)
        clear()
        option2()       
start()
