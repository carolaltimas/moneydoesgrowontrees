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
    night()


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







## Afternoon ##

## Night ##
required = "\nUse only a, b, or c\n"  # Cutting down on duplication
# The story is broken into sections, starting with "intro"
def night():
    print("-" * 80)
    print(""" It was a long day at school. You're hungry. You want a snack. You head to your kitchen.What should you have? """)
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
    print("""You have some time to kill before dinner. You finished up your homework at school. You decide to watch some TV. You're torn between watching Victorious or iCarly. You realize that you could use both or either, but you only have time for two episodes. You remember a principle you learned 
     at school called "Opportunity Cost." It is the loss of potential gain from other alternatives when one alternative is chosen. If you only watch Victorious, the opportunity cost is watching two episodes of iCarly. If you only pick iCarly, the opportunity cost is 
     two episodes of Victorious. You're a little confused on what to pick. What will you do?""")
    print("  a. Watch two episodes of Victorious")
    print("  b. Watch two episodes of iCarly")
    print("  c. Watch one episode of iCarly and one episode of Victorious")
    
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print("""Great choice! You love Victorious! You spend time singing along to the songs and 
        your sister Jane even comes to join you!""")
        night_3()
    elif choice in answer_B:
        print("""Awesome choice! iCarly is showing that episode where her room is redone!  
        You spend time singing along to the songs and your sister Jane even comes to watch!""")
        night_3()
    elif choice in answer_C:
        print("""Awesome choice! iCarly is showing that episode where her room is redone 
        and Victorious is showing your favourite episode!""")
        night_3()
    else:
        print(required)
        night_2()


# night 3 action
def night_3():
    print("-" * 80)
    print("""It's dinnertime. You leave the TV room, but forget to turn off the lights. You're almost at the dinnertable, but you can go back and turn off the lights. What will you do?"""
    )
    print("  a. Go back and turn off the lights.")
    print("  b. Ignore the lights and go have dinner.")
    choice = input(">>> ")  # input of the choice
    global green_points
    if choice in answer_A:
        print("""Awesome choice! Turning off the lights is one of the small decisions that helps the environment every day! You get one green point!""")
        green_points = green_points + 1
        night_4()
    elif choice in answer_B:
        print(""" The lights shine through the door of the TV room. Your sister Jane notices and goes to turn them off. You should have turned them off earlier. You lose one green point.""")
        green_points = green_points - 1
        night_4()
    else:
        print(required)
        night_3()


# night 4 action
def night_4():
    print("-" * 80)
    print(""" It's getting late. You're about to head to bed, but your sister Jane stops you in the corridor. She's talking about how she wants to get the ps5 again.
  This is the only topic on her mind these days. Your mom gave you each some Christmas money to buy things, but Jane doesn't have enough for the ps5 yet.
  Her birthday's coming up, so she'll probably have enough soon. Her tone changes. "I really want to get the WII as well. Could I buy that tonight?" What should you do? """)
    print("  a. You remind Jane of her long term goal of getting the ps5 and tell her to hold off on getting the WII. ")
    print("  b. You cave and tell her to get the WII. She probably won't be able to buy the ps5 later on, but who cares about her long term goal? ")
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print(
            "Great Choice! Jane remembers how much she wants the ps5 and agrees that she should save up instead."
        )
        night_5()
    elif choice in answer_B:
        print(
            """You begin the process of buying the WII online. Once bought, Jane remembers how much she wanted the ps5 and regrets the WII decision.
    Jane realizes that she completely forgot her longterm goal and is a little disappointed, but she's okay with getting the WII in the end."""
        )
        night_5()
    else:
        print(required)
        night_4()


# night 5 action
def night_5():
    print("-" * 80)
    print("""  You've finally made it to bed. You lay down under the covers and notice that you're feeling a little cold. BURRRRRR. It's not winter-level cold, but it's going to bother you. You decide to do something about it, 
    since you know that you can't sleep when it's cold. You probably could do without turning on the heat. """
    )
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
    print('\n'"The day is done!")
    print("Money Remaining: ", int(money))
    print("Chequing Account Balance: ", int(chequings_acc))
    print("Savings Account Balance: ", int(savings_acc))
    print("Green Points Collected: ", int(green_points))

    
    

main()

