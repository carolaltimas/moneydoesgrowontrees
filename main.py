## Project: Money Does Grow On Trees ##
## Authors: Aranya Sutharsan, Rinoa Malapaya Noshin Rahman, Carol Altimas ##

import time  # Imports a module to add a pause
from morning import *

# User Responses
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

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
    answer_A = ["A", "a"]
    answer_B = ["B", "b"]
    answer_C = ["C", "c"]
    yes = ["y", "yes"]
    no = ["n", "no"]
    intro()
    afternoon()
    night()
    one_month_later()
    six_months_later()
    one_year_later()


def intro():
    print("Welcome to Money Does Grows On Trees!")
    print("-" * 80)

    print("As you play along in this game you will be collecting and losing money based on the financial "
          "decisions you made.")
    print("As well as collecting and losing green points based on your environmental decisions.")
    print()

    print("You will be given 5 Green points from the start :)")
    print("You have also saved $1000 from Christmas / Birthdays / Weekly allowances / doing chores! Nice job!")
    print("-" * 80)

    print("Before the game starts, here are some terminology!")
    print()
    print("  1. Savings accounts are bank accounts that pay interest on the money you deposit.")
    print()
    print("  2. Interest is your reward for steady and consistent saving!")
    print("   - the more money you put in, the more interest you earn, and the more your balance will grow.")
    print()
    print("  3. High-growth interest is still a savings account")
    print("   - however, it pays a little bit more interest compared to a regular savings account!")
    print("-" * 80)
    print("Now let's start the game!")
    introQn()


def verifyIntro():
    print("How much would you like to set aside?")
    extraChoice = input(">>> ")

    if extraChoice.isdigit():

        if float(extraChoice) < 0 or float(extraChoice) == 0:
            print("Invalid input. Please enter an amount greater than 0.")
            print()
            verifyIntro()

        if float(extraChoice) > 1000:
            print("Invalid input. Please enter an amount less than 1000.")
            print()
            verifyIntro()

        if 0 < float(extraChoice) <= 1000:
            print("-" * 80)
            global savings_acc
            global chequings_acc
            savings_acc = float(extraChoice)
            chequings_acc = 1000 - savings_acc
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
        print()
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
    global chequings_acc

    if choice.lower() in answer_A:
        print("Note: Nice choice! Bagel cost $2.20 plus tax this would equal up to $2.5.")
        chequings_acc = float(chequings_acc) - 2.50
        print("-" * 80)
        morning3Good()

    elif choice.lower() in answer_B:
        print("Great choice to boost up your energy for the day!")
        print("   - Coffee cost $1.60 plus tax this would equal to $1.80.!")
        print("   - This is the cheapest option too! Nice job :)")
        chequings_acc = float(chequings_acc) - 1.80
        print("-" * 80)
        morning3Good()

    elif choice.lower() in answer_C:
        print("You’re set for the day!")
        print("   - Although this combo might seem like a steal, the final is actually $3.95! Not bad.")
        chequings_acc = float(chequings_acc) - 3.95
        print("-" * 80)
        morning3Good()

    else:
        print("Invalid input! Please type a, b or c")
        print()
        morning3BadQn()


def morning4():
    print("While walking to your classroom, you see a fellow classmate throw their garbage on the floor.")
    morning4Qn()


def morning4Qn():
    print("What would you do? ")
    print("a. Tell the student to pick up the garbage")
    print("b. You throw away classmate's garbage")
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
        print()
        morning4Qn()


def morningSummary():
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    print("Green Points Collected: ", float(green_points))



## Afternoon ##


## Night ##
required = "\nUse only a, b, or c\n"  # Cutting down on duplication
# The story is broken into sections, starting with "intro"
def night():
    
    print("-" * 80)
    print("""It was a long day at school. You're hungry. You want a snack.""")
    print("You head to your kitchen.")
    print("What should you have?")
    print("  a. A homemade chocolate chip cookie! It is the love of your life!")
    print("  b. A bowl of frozen grapes. A little weird, but it tastes like candy!")
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print("Excellent choice! It was delicious!")
        night_2()
    elif choice in answer_B:
        print("Yessss frozen grapes! ")
        night_2()
    else:
        print(required)
        night()


# next action is
def night_2():
    print("-" * 80)
    print("You have some time to kill before dinner. You finished up your homework at school.")
    print("You decide to watch some TV. You're torn between watching Victorious or iCarly and you only have time for two episodes.")
    print("You realize that you can use a financial term called Opportunity Cost to decide.")
    print("Opportunity Cost is the loss of potential gain from other alternatives when one alternative is chosen.")
    print("For example, if you only watch Victorious, the opportunity cost is two episodes of iCarly, since you would be missing out on watching two episodes of iCarly")
    print("For example, if you only pick iCarly, the opportunity cost is two episodes of Victorious.")
    print("What should you do?")
    print("  a. Watch two episodes of Victorious")
    print("  b. Watch two episodes of iCarly")
    print("  c. Watch one episode of iCarly and one episode of Victorious")
    
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print("Great choice! You spend time singing along to the songs!")
        print("Your sister Jane even comes and sings along")
        night_3()
    elif choice in answer_B:
        print("Awesome choice! iCarly is showing that episode where her room is redone!")
        print("You spend time singing along to the songs and your sister Jane even comes to watch!")
        night_3()
    elif choice in answer_C:
        print("Awesome choice! iCarly is showing that episode where her room is redone") 
        print("Victorious even shows your favourite episode!")
        night_3()
    else:
        print(required)
        night_2()


# night 3 action
def night_3():
    print("-" * 80)
    print("It's dinnertime. You leave the TV room, but forget to turn off the lights.")
    print("You're almost at the dinner table, but you can go back and turn off the lights. What will you do?")
    print("What will you do?")
    print("  a. Go back and turn off the lights.")
    print("  b. Ignore the lights and go have dinner.")
    choice = input(">>> ")  # input of the choice
    global green_points
    if choice in answer_A:
        print("""Awesome choice! Turning off the lights is one of the small decisions that helps the environment every day!""")
        print("""You get one green point!""")
        green_points = green_points + 1
        night_4()
    elif choice in answer_B:
        print(""" The lights shine through the door of the TV room. Your sister Jane notices and goes to turn them off.""")
        print("""You should have turned them off earlier. You lose one green point.""")
        green_points = green_points - 1
        night_4()
    else:
        print(required)
        night_3()


# night 4 action
def night_4():
    print("-" * 80)
    print("It's getting late. You're about to head to bed, but your sister Jane stops you in the corridor.")
    print("She's talking about how she wants to get the ps5 again.This is the only topic on her mind these days. ")
    print("Your mom gave you each some Christmas money to buy things, but Jane doesn't have enough for the ps5 yet and you're in charge on the finances")
    print("Her birthday's coming up, so she'll probably have enough soon. Her tone changes. ")
    print("I really want to get the WII as well. Could I buy that tonight?" "What should you do?")
    print("  a. You remind Jane of her long term goal of getting the ps5 and tell her to hold off on getting the WII. ")
    print("  b. You cave and tell her to get the WII. She probably won't be able to buy the ps5 later on, but who cares about her long term goal? ")
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print(
            "Great Choice! Jane remembers how much she wants the ps5 and agrees that she should save up instead."
        )
        night_5()
    elif choice in answer_B:
        print("""You begin the process of buying the WII online. Once bought, Jane remembers how much she wanted the ps5 and regrets the WII decision.""")
        print("""Jane realizes that she completely forgot her longterm goal and is a little disappointed, but she's okay with getting the WII in the end.""")
        night_5()
    else:
        print(required)
        night_4()


# night 5 action
def night_5():
    print("-" * 80)
    print("""You've finally made it to bed. You lay down under the covers and notice that you're feeling a little cold.""")
    print("""BURRRRRR. It's not winter-level cold, but it's going to bother you.""")
    print("""You decide to do something about it, since you know that you can't sleep when it's cold.""")
    print("""What do you do?""")
    print("  a. Grab a warm blanket from the linen closet.")
    print("  b. Change into your favourite warm pjs.")
    print("  c. Turn up the heat.")

    global green_points
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print("Good choice! You begin to feel warm and can finally sleep! ")
        print(
            "By using less heat, you're helping the environment. You get one green point!"
        )
        green_points = green_points + 1
        end_of_night()
    elif choice in answer_B:
        print("YESSS!! warmth finally. It feels so good to be in your favourite pjs.")
        print(
            "By not turning up the heat and wearing your pjs, you're helping the enviroment. Here's a green point!"
        )
        green_points = green_points + 1
        end_of_night()
    elif choice in answer_C:
        print("You can feel the heat instantly. ")
        print(
            "You knew you probably didn't need to turn on the heat, since it wasn't too cold. You lose one green point."
        )
        green_points = green_points - 1
        end_of_night()
    else:
        print(required)
        night_5()


def end_of_night():
    print('\n'"You finally fall asleep.")
    print('\n'"The first day is done")
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    print("Green Points Collected: ", float(green_points))

def one_month_later():
    global savings_acc
    savings_acc = interestformula(savings_acc, float(0.05), (1/12))

    print('\n'"If you continue your actions for a month. Your account would look like...")
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    temp_green_points = green_points * 30 * 1
    print("Green Points Collected: ", float(temp_green_points))

def six_months_later():
    global savings_acc
    savings_acc = interestformula(savings_acc, float(0.01),(6/12))
    print('\n'"If you continue your actions for six months. Your account would look like...")
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    temp_green_points = green_points * 30 * 6
    print("Green Points Collected: ", float(temp_green_points))
    

def one_year_later():
    global savings_acc
    savings_acc = interestformula(savings_acc, float(0.01),(6/12)) 

    print('\n'"If you continue your actions for a year. Your account would look like...")
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    temp_green_points = green_points * 30 * 12
    print("Green Points Collected: ", float(temp_green_points))
    


def interestformula(given_money, interest, time):
    temp = given_money
    inner_equation = 1 + (time/12)
    exponent = (12 * time)
    current_money = inner_equation ** exponent
    current_money = temp * current_money
    return current_money



main()

