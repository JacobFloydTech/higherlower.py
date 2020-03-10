
import random
import os 
import sys
import time
listofnumbers = []
os.system('clear')
number = random.randint(1,100)

def type(string):
  for char in string:  
    sys.stdout.write(char)
    sys.stdout.flush() 
    time.sleep(0.08)

def start():
    type("Welcome! \n")
    type("Do you want the rounds to be limited or to count you? Please type 1 for limited and 2 for unlimited")
    option = input("")
    if option == '1':
        option1()
    elif option == '2':
        option2()


def option1():
    try:
        rounds = 10
        while rounds > 0:
            guess = input("Number")
            if int(guess) in listofnumbers:
                print(listofnumbers)
                print("Already used number!")
                guess = input("Number")
            elif int(guess) not in listofnumbers:
                listofnumbers.append(int(guess))
                if int(guess) == number:
                    print("Won")
                    print("You did it with %s rounds left!" % rounds)
                    break
                elif int(guess) > number:
                    print("too high")
                    rounds -= 1
                    print("You have %s rounds left" % rounds)
                elif int(guess) < number:
                    print("Too low")
                    rounds -= 1
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
        os.system('clear')
        option1()


def option2():
    rounds = 0
    os.system('clear')
    while rounds == 0 or rounds > 0:
        guess = input("Number")
        if int(guess) in listofnumbers:
            print("You have already used that number before")
            print(listofnumbers)
        elif int(guess) not in listofnumbers:
            listofnumbers.append(int(guess))
            if int(guess) > number:
                print("Too high")
                rounds += 1
                print("This was round " + str(rounds))
            elif int(guess) < number:
                print("Too low")
                rounds += 1
                print("This was round" + str(rounds))
            elif int(guess) == number:
                print("You got it! It was " + str(number))
                playagain = input("Do you wanna play again?")
                if playagain.lower() == 'yes' or 'y':
                    start()
                elif playagain.lower() == 'no' or 'n':
                    sys.exit()
                else:
                    print("Please do yes, y, no or n")
                    playagain = input("Do you want to play again?")
start()