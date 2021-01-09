## Project: Money Does Grow On Trees ##
## Authors: Aranya Sutharsan, Rinoa Malapaya Noshin Rahman, Carol Altimas ##

import time  # Imports a module to add a pause

# User Responses
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Variables for the game
green_points = 0
chequings_acc = 1000
savings_acc = 0
money = 0


## Introduction + Morning##
# Main Functions - calls all functions
def main():
    global green_points
    global money
    global answer_A
    global answer_B
    global answer_C
    global yes
    global no
    global savings_acc
    global chequings_acc
    global credit_avail
    green_points = 5
    money = 1000
    answer_A = ["a"]
    answer_B = ["b"]
    answer_C = ["c"]
    yes = ["y", "yes"]
    no = ["n", "no"]
    intro()


def intro():
    print("Welcome to Money Does Grows On Trees!")
    print("-" * 80)

    print("As you play along in this game you will be collecting and losing money based on the financial "
          "decisions you made.")
    print("As well as collecting and losing green points based on your environment decisions.")
    print()

    print("You will be given 5 Green points from the start :)")
    print("You have also saved $1000 from Christmas / Birthdays / Weekly allowances / doing chores! Nice job!")
    print("-" * 80)

    print("Before the game starts, here are some terminology!")
    print()
    print("1. Savings accounts are bank accounts that pay interest on the money you deposit.")
    print()
    print("2. Interest is your reward for steady and consistent saving!")
    print("   - the more money you put in, the more interest you earn, and the more your balance will grow.")
    print()
    print("3. High-growth interest is still a savings account")
    print("   - however, it pays a little bit more interest compared to a regular savings account!")
    print("-" * 80)
    print("Now let's start the game!")
    introQn()


def verifyIntro():
    print("How much would you like to set aside?")
    extraChoice = input(">>> ")
    global money

    if extraChoice.isdigit():

        if int(extraChoice) < 0 or int(extraChoice) == 0:
            print("Invalid input. Please enter an amount greater than 0.")
            print()
            verifyIntro()

        if int(extraChoice) > int(money):
            print("Invalid input. Please enter an amount less than 1000.")
            print()
            verifyIntro()

        if 0 < int(extraChoice) <= int(money):
            print("-" * 80)
            global savings_acc
            global chequings_acc
            savings_acc = int(extraChoice)
            money = 1000 - savings_acc
            chequings_acc = int(money)
            morning1()

    else:
        print("Invalid input. Please enter a digit!")
        print()
        verifyIntro()


def introQn():
    print()
    print("Would you like to set aside some amount of money to your savings account?")
    choice = input(">>> ")

    if choice.lower() in yes:
        print()
        verifyIntro()

    elif choice.lower() in no:
        print("Note: Setting aside some money in your savings account would have been great in the long run!")
        print("   - The more money you set aside, the higher interest / return you'd have :)")
        print("-" * 80)
        morning1()

    else:
        print("Invalid input! Please type yes/no OR y/n")
        introQn()


def morning1():
    print("It’s Monday morning and you just woke up from a lovely nap.")
    print("You have done your morning routine, and are ready to go to school.")
    print()
    morning1Qn()


def morning1Qn():
    print("Do you want to buy breakfast (a) or make a healthy breakfast at home (b)?")
    choice = input(">>> ")

    if choice.lower() in answer_A:
        print("Note: A better choice could have been to make a meal at home!")
        print("   - It is always great to save whenever you can :)")
        print("-" * 80)
        morning2Bad()

    elif choice.lower() in answer_B:
        print("Great Choice! Hope you have a great breakfast :)")
        print("-" * 80)
        morning2Good()

    else:
        print("Invalid input! Please type a or b")
        print()
        morning1Qn()


def morning2Bad():
    print("Do you want to walk to the cafe (a)? Or want to take a bus to the cafe (b)?")
    choice = input(">>> ")
    global green_points

    if choice.lower() in answer_B:
        print("Note: It would have been more eco friendly to walk!")
        print("   - By taking public transportation, we are contributing more carbon footprint :(")
        print()

        print("Unfortunately, a green point will be removed!")
        green_points = green_points - 1
        print("-" * 80)
        morning3Bad()

    elif choice.lower() in answer_A:
        print("Excellent choice, by walking you are helping mother nature by reducing carbon footprint :)")
        print("   - Enjoy the view!")
        print()

        print("Congrats you have received a green point for doing a good deed!")
        green_points = green_points + 1
        print("-" * 80)
        morning3Bad()

    else:
        print("Invalid input! Please type a or b")
        print()
        morning1Qn()


def morning2Good():
    print("You enjoyed your healthy breakfast along with your family.")
    print("However you still have time before school starts.")
    print()
    morning2GoodQn()


def morning2GoodQn():
    print("Would you like to play a fun game of 'Among Us'?")
    choice = input(">>> ")

    if choice.lower() in yes:
        print("Hope you have fun!")
        print("-" * 80)
        morning3Good()

    elif choice.lower() in no:
        print("Ohh that a bummer!")
        print("-" * 80)
        morning3Good()

    else:
        print("Invalid input! Please type yes/no OR y/n")
        morning2GoodQn()


def morning3Good():
    print("After moments of travelling, you finally reached school.")
    morning4()
    print("-" * 80)


def morning3Bad():
    print("Once you walk into the cafe, you spot the menu.")
    print("Bagel: $2.20 (a) | Coffee: $1.60 (b) | Both: $3.50 (c)")
    print()
    print("Now it's time to decide what you would like to eat!")
    print()
    morning3BadQn()


def morning3BadQn():
    print("What would you like to have?")
    choice = input(">>> ")
    global money
    global chequings_acc

    if choice.lower() in answer_A:
        print("Note: Nice choice! Bagel cost $2.20 plus tax this would equal up to $2.5.")
        money = int(money) - 2.20
        chequings_acc = int(chequings_acc) - 2.20
        print("-" * 80)
        morning3Good()

    elif choice.lower() in answer_B:
        print("Great choice to boost up your energy for the day!")
        print("   - Coffee cost $1.60 plus tax this would equal to $1.60.!")
        print("   - This is the cheapest option too! Nice job :)")
        money = int(money) - 1.60
        chequings_acc = int(chequings_acc) - 1.60
        print("-" * 80)
        morning3Good()

    elif choice.lower() in answer_C:
        print("You’re set for the day!")
        print("   - Although this combo might seem like a steal, the final is actually $3.50! Not bad.")
        money = int(money) - 3.50
        chequings_acc = int(chequings_acc) - 3.50
        print("-" * 80)
        morning3Good()

    else:
        print("Invalid input! Please type a, b or c")
        morning3BadQn()


def morning4():
    print("While walking to your classroom, you see a fellow classmate throw their garbage on the floor.")
    morning4Qn()


def morning4Qn():
    print("What would you do? ")
    print("a. Tell the student to pick up the garbage")
    print("b. You throw away classmate garbage")
    print("c. Ignore the garbage and walk away")
    choice = input(">>> ")
    global green_points

    if choice.lower() in answer_A:
        print("Good job for raising awareness!")
        print()
        green_points = green_points + 1
        print("Congrats you have received a green point for doing a good deed!")
        print("-" * 80)
        morningSummary()

    elif choice.lower() in answer_B:
        print("Thank you for being a good citizen! ")
        print()
        green_points = green_points + 1
        print("Congrats you have received a green point for doing a good deed!")
        print("-" * 80)
        morningSummary()

    elif choice.lower() in answer_C:
        print("Littering can cause a serious aftermath for the environment.")
        print("   - such as pollution, kills wildlife and many more.")
        print()
        green_points = green_points - 1
        print("Unfortunately, a green point will be removed!")
        print("-" * 80)
        morningSummary()

    else:
        print("Invalid input! Please type a, b or c")
        morning4Qn()


def morningSummary():
    print("Money Remaining: ", int(money))
    print("Chequing Account Balance: ", int(chequings_acc))
    print("Savings Account Balance: ", int(savings_acc))
    print("Green Points Collected: ", int(green_points))


main()




## Afternoon ##

## Night ##
