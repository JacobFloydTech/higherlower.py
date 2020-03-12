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

def type(string):
  for char in string:  
    sys.stdout.write(char)
    sys.stdout.flush() 
    time.sleep(0.06)

def start():
    clear()
    type("Welcome! \n")
    type("Do you want the rounds to be limited or to count you? Please type 1 for limited and 2 for unlimited rounds:  \n")
    option = input("")
    if option == '1':
        option1()
    elif option == '2':
        option2()
    elif option != '1' or option != '2':
        type("Please either use 1 or 2") 
        option = input("")

def option1():
    try:
        type("Do you want to set a max value for the number?")
        optionx = input("")
        if optionx.lower() == 'y':
            optiony = input("Number : ")
            secret_number = random.randint(1, int(optiony))
        elif optionx.lower() == 'n':
            secret_number = random.randint(1,100)
        rounds = 10
        print(secret_number)
        guesses = 1
        while rounds > 0:
            guess = input("Number ")
            if int(guess) in listofnumbers:
                print(listofnumbers)
                print("Already used number!")
                guess = input("Number ")
            elif int(guess) not in listofnumbers:
                listofnumbers.append(int(guess))
                if int(guess) == secret_number:
                    print("Won")
                    if guesses == 1:
                        print("You did it in 1 round!")
                    else:
                        print("You did it in %s rounds" % guesses)
                    break
                elif int(guess) > secret_number:
                    clear()
                    print("Too high")
                    rounds -= 1
                    guesses += 1 
                    print("You have %s rounds left" % rounds)
                elif int(guess) < secret_number:
                    clear()
                    print("Too low")
                    rounds -= 1
                    guesses += 1
                    print("You have %s rounds left" % rounds)
        print("Number to get was " + str(secret_number))
        play_again = input("Play again? Y/N")
        if play_again.upper() == 'Y':
            clear()
            listofnumbers.clear()
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
        type("Do you want to set a max value for the number?")
        optionx = input("")
        if optionx.lower() == 'y':
            optiony = input("Number : ")
            secret_number = random.randint(1, int(optiony))
        elif optionx.lower() == 'n':
            secret_number = random.randint(1,100)
        guesses = 1
        rounds = 1
        clear()
        print(secret_number)
        while rounds == 0 or rounds > 0:
            print("Round %s" % str(rounds))
            guess = input("Number ")
            if int(guess) in listofnumbers:
                print("You have already used that number before")
                print(listofnumbers)
            elif int(guess) not in listofnumbers:
                listofnumbers.append(int(guess))
                if int(guess) > secret_number:
                    clear()
                    print("Too high")
                    rounds += 1
                    guesses += 1
                elif int(guess) < secret_number:
                    clear()
                    print("Too low")
                    rounds += 1
                    guesses += 1
                elif int(guess) == secret_number:
                    clear()
                    print("You got it! It was " + str(secret_number))
                    print("You did it in %s guesses" % guesses)
                    playagain = input("Do you wanna play again?")
                    if playagain.lower() == 'yes' or playagain.lower() == 'y':
                        clear()
                        listofnumbers.clear()
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
