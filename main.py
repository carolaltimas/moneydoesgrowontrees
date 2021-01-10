## Project: Money Does Grow On Trees ##
## Authors: Aranya Sutharsan, Rinoa Malapaya Noshin Rahman, Carol Altimas ##

import time  # Imports a module to add a pause

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
credit_balance = 0
credit_avail = 0
reward_pts = 0


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
    global credit_balance
    global reward_pts
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
    time.sleep(1)

    print("As you play along in this game you will be collecting and losing money based on the financial "
          "decisions you made.")
    print("As well as collecting and losing green points based on your environmental decisions.")
    time.sleep(2)
    print()

    print("You will be given 5 Green points from the start :)")
    print("You have also saved $1000 from Christmas / Birthdays / Weekly allowances / doing chores! Nice job!")
    time.sleep(2)
    print("-" * 80)

    print("Before the game starts, here are some terminology!")
    time.sleep(1.5)
    print()
    print("  1. Savings accounts are bank accounts that pay interest on the money you deposit.")
    time.sleep(1.5)
    print()
    print("  2. Interest is your reward for steady and consistent saving!")
    print("   - the more money you put in, the more interest you earn, and the more your balance will grow.")
    time.sleep(1.5)
    print()
    print("  3. High-growth interest is still a savings account")
    print("   - however, it pays a little bit more interest compared to a regular savings account!")
    time.sleep(1.5)
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
            time.sleep(1)
            verifyIntro()

        if float(extraChoice) > 1000:
            print("Invalid input. Please enter an amount less than 1000.")
            print()
            time.sleep(1)
            verifyIntro()

        if 0 < float(extraChoice) <= 1000:
            print("-" * 80)
            global savings_acc
            global chequings_acc
            savings_acc = float(extraChoice)
            chequings_acc = 1000 - savings_acc
            time.sleep(1)
            morning1()

    else:
        print("Invalid input. Please enter a digit!")
        print()
        time.sleep(1)
        verifyIntro()


def introQn():
    time.sleep(1.5)
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
        time.sleep(2)
        morning1()

    else:
        print("Invalid input! Please type yes/no OR y/n")
        time.sleep(1)
        introQn()


def morning1():
    print("It’s Monday morning and you just woke up from a lovely nap.")
    print("You have done your morning routine, and are ready to go to school.")
    time.sleep(2)
    print()
    morning1Qn()


def morning1Qn():
    print("Do you want to buy breakfast (a) or make a healthy breakfast at home (b)?")
    choice = input(">>> ")

    if choice.lower() in answer_A:
        print("Note: A better choice could have been to make a meal at home!")
        print("   - It is always great to save whenever you can :)")
        time.sleep(2)
        print("-" * 80)
        morning2Bad()

    elif choice.lower() in answer_B:
        print("Great Choice! Hope you have a great breakfast :)")
        time.sleep(1)
        print("-" * 80)
        morning2Good()

    else:
        print("Invalid input! Please type a or b")
        print()
        time.sleep(1)
        morning1Qn()


def morning2Bad():
    print("Do you want to walk to the cafe (a)? Or want to take a bus to the cafe (b)?")
    choice = input(">>> ")
    global green_points

    if choice.lower() in answer_B:
        print("Note: It would have been more eco friendly to walk!")
        print("   - By taking public transportation, we are contributing more carbon footprint :(")
        time.sleep(2)
        print()

        print("Unfortunately, a green point will be removed!")
        green_points = green_points - 1
        time.sleep(1)
        print("-" * 80)
        morning3Bad()

    elif choice.lower() in answer_A:
        print("Excellent choice, by walking you are helping mother nature by reducing carbon footprint :)")
        print("   - Enjoy the view!")
        print()
        time.sleep(2)

        print("Congrats you have received a green point for doing a good deed!")
        green_points = green_points + 1
        time.sleep(1)
        print("-" * 80)
        morning3Bad()

    else:
        print("Invalid input! Please type a or b")
        print()
        time.sleep(1)
        morning1Qn()


def morning2Good():
    print("You enjoyed your healthy breakfast along with your family.")
    print("However you still have time before school starts.")
    print()
    time.sleep(2)
    morning2GoodQn()


def morning2GoodQn():
    print("Would you like to play a fun game of 'Among Us'?")
    choice = input(">>> ")

    if choice.lower() in yes:
        print("Hope you have fun!")
        time.sleep(0.5)
        print("-" * 80)
        morning3Good()

    elif choice.lower() in no:
        print("Ohh that a bummer!")
        time.sleep(0.5)
        print("-" * 80)
        morning3Good()

    else:
        print("Invalid input! Please type yes/no OR y/n")
        print()
        time.sleep(1)
        morning2GoodQn()


def morning3Good():
    print("After moments of travelling, you finally reached school.")
    morning4()
    print("-" * 80)


def morning3Bad():
    print("Once you walk into the cafe, you spot the menu.")
    print("Bagel: $2.20 (a) | Coffee: $1.60 (b) | Both: $3.50 (c)")
    print()
    time.sleep(2)
    print("Now it's time to decide what you would like to eat!")
    print()
    time.sleep(1)
    morning3BadQn()


def morning3BadQn():
    print("What would you like to have?")
    choice = input(">>> ")
    global chequings_acc

    if choice.lower() in answer_A:
        print("Note: Nice choice! Bagel cost $2.20 plus tax this would equal up to $2.5.")
        chequings_acc = float(chequings_acc) - 2.50
        time.sleep(1.5)
        print("-" * 80)
        morning3Good()

    elif choice.lower() in answer_B:
        print("Great choice to boost up your energy for the day!")
        print("   - Coffee cost $1.60 plus tax this would equal to $1.80.!")
        print("   - This is the cheapest option too! Nice job :)")
        chequings_acc = float(chequings_acc) - 1.80
        time.sleep(2.5)
        print("-" * 80)
        morning3Good()

    elif choice.lower() in answer_C:
        print("You’re set for the day!")
        print("   - Although this combo might seem like a steal, the final is actually $3.95! Not bad.")
        chequings_acc = float(chequings_acc) - 3.95
        time.sleep(1.5)
        print("-" * 80)
        morning3Good()

    else:
        print("Invalid input! Please type a, b or c")
        print()
        time.sleep(1)
        morning3BadQn()


def morning4():
    print("While walking to your classroom, you see a fellow classmate throw their garbage on the floor.")
    time.sleep(2)
    morning4Qn()


def morning4Qn():
    print('\n'"What would you do? ")
    time.sleep(0.5)
    print("  a. Tell the student to pick up the garbage")
    time.sleep(1)
    print("  b. You throw away classmate's garbage")
    time.sleep(1)
    print("  c. Ignore the garbage and walk away")
    time.sleep(1)
    choice = input(">>> ")
    global green_points

    if choice.lower() in answer_A:
        print("Good job for raising awareness!")
        print()
        time.sleep(0.5)
        green_points = green_points + 1
        print("Congrats you have received a green point for doing a good deed!")
        time.sleep(1)
        print("-" * 80)
        morningSummary()

    elif choice.lower() in answer_B:
        print("Thank you for being a good citizen! ")
        print()
        time.sleep(0.5)
        green_points = green_points + 1
        print("Congrats you have received a green point for doing a good deed!")
        time.sleep(1)
        print("-" * 80)
        morningSummary()

    elif choice.lower() in answer_C:
        print("Littering can cause a serious aftermath for the environment.")
        print("   - such as pollution, kills wildlife and many more.")
        print()
        time.sleep(2)
        green_points = green_points - 1
        print("Unfortunately, a green point will be removed!")
        time.sleep(1)
        print("-" * 80)
        morningSummary()

    else:
        print("Invalid input! Please type a, b or c")
        time.sleep(1)
        morning4Qn()


def morningSummary():
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    print("Green Points Collected: ", float(green_points))
    time.sleep(2)


## Afternoon ##
def afternoon():
    print(
        "Now that you've developed ideal basic spending and saving habits, your parents have decided to provide you with your very first Credit Card! "'\n')
    print("Here is what you should know about Credit:")
    time.sleep(2)
    print("  1. The money on your credit card is not your money, but the bank's money so it isn't free.")
    print(
        "When you use your Credit Card to make purchases, the bank is letting you borrow some amount of money to spend that must be paid back eventually.")
    print(
        " After the 21 day grace period, the longer it takes you to pay back the balance, the balance, the more the interest will add up."'\n')
    time.sleep(3)
    print("  2. There's a limit to HOW MUCH you can purchase on your credit card.")
    print(
        "It is known as a credit limit ($500 in your case) and is the maximum amount of money you can borrow at a time from the bank.")
    print("Keeping a low credit card balance makes it easier to pay off and build a better credit history."'\n')
    time.sleep(3)
    print("  3. You're being graded.")
    print(
        "Everybody who uses a credit card has a credit score which is based on your credit card history (how frequently you make payments, outstanding loans, your available credit etc.)")
    print("It ranges on average from 300 to 850, with higher credit scores being better.")
    print(
        "Having a good credit score gives you benefits such as approval for loans in the future for a mortgage for a new houseor buying a new car, better interest rates on your loans and more."'\n')
    time.sleep(3)
    global credit_balance
    afternoon1()


def afternoon1():
    print("-" * 80)
    print("The Spring Homecoming dance is coming up and you don't have a dress for the occasion.")
    print(
        "Your friends offer you some dresses for you to borrow or offer to go to the mall this afternoon so you could buy a brand new one yourself.")
    print('\n'"What will you do?")
    time.sleep(2)
    print("  a. Stick with some existing options for dresses from your kind friends.")
    time.sleep(1)
    print("  b. Go to the mall with them so you can all purchase a new one for the dance.")
    time.sleep(1)
    choice = input(">>> ")
    if choice.lower() in answer_A:
        option_oldDress()
    elif choice.lower() in answer_B:
        option_newDress()
    else:
        print("Invalid input! Please type a, b, or c")
        time.sleep(1)
        afternoon1()


def option_oldDress():
    print("Great choice! You saved money buy choosing not to buy a new dress and rather borrow one instead.")
    print("Additionally, by not having to travel to the mall, you reduce your carbon emissions by saving your fuel.")
    time.sleep(2)
    global green_points
    green_points += 5
    afternoon2()


def option_newDress():
    print(
        "Sounds fun! Although there was a missed opportunity to save money on purchasing a new dress entirely, we can continue finding other options that are financially smart!")
    time.sleep(2)
    global green_points
    green_points -= 2
    afternoon2()


def afternoon2():
    print("-" * 80)
    print("You have settled on 3 options that you love:")
    time.sleep(1)
    print("  a. A long red maxi dress at $40.")
    time.sleep(1)
    print("  b. A blue bell-sleeve dress at $50.")
    time.sleep(1)
    print("  c. A black off-the-shoulder dress at $70.")
    time.sleep(1)
    print('\n'"Which dress do you choose: ")
    choice = input(">>> ")

    if choice.lower() in answer_A:
        option_redDress()
    elif choice.lower() in answer_B:
        option_blueDress()
    elif choice.lower() in answer_C:
        option_blackDress()
    else:
        print("Invalid input!")
        time.sleep(0.5)
        afternoon2()


def pay():
    print("-" * 80)
    print('\n'"You can choose to complete this purchase with your debit card or your new credit card."'\n')
    print("Here are some tips to keep in mind."'\n')
    time.sleep(2)
    print(
        "Credit: By using a credit card for shopping purchases, you can gain reward points based on each dollar you spent at certain retailers."'\n')
    time.sleep(2)
    print(
        "By accumulating points later on, you can redeem them for other purchases without having to spent real money or use it to pay off your credit card.")
    print(
        "However you do have to make sure you pay off the purchase eventually with your own money. If you're unable to do so in time, you will be charged interest.")
    time.sleep(2)
    print(
        '\n'"Debit: By using your debit card, you are spending your own money and won't have to worry about any remaining payments after the purchase.")
    print("But you may miss out on the opportunity to collect reward points.")
    time.sleep(2)


def option_redDress():
    print("Beautiful choice and economic purchase!")
    time.sleep(1)
    pay()
    print('\n'"How would you like to pay?")
    time.sleep(1)
    print("  a. Debit Card")
    print("  b. Credit Card")
    choice = input(">>> ")

    global credit_avail
    global credit_balance
    global chequings_acc
    global reward_pts
    credit_avail = 500

    if choice.lower() in answer_A:
        chequings_acc -= 40
        afternoon3()
    elif choice.lower() in answer_B:
        credit_avail -= 40
        credit_balance += 40
        reward_pts += 40
        afternoon3()
    else:
        print("Invalid input!")
        time.sleep(0.5)
        option_redDress()


def option_blueDress():
    print("Lovely pick at a relatively good price!")
    time.sleep(1)
    pay()
    print('\n'"How would you like to pay?")
    time.sleep(1)
    print("  a. Debit Card")
    print("  b. Credit Card")
    choice = input(">>> ")

    global credit_avail
    global credit_balance
    global chequings_acc
    global reward_pts
    credit_avail = 500

    if choice.lower() in answer_A:
        chequings_acc -= 50
        afternoon3()
    elif choice.lower() in answer_B:
        credit_avail -= 50
        credit_balance += 50
        reward_pts += 50
        afternoon3()
    else:
        print("Invalid input!")
        time.sleep(0.5)
        option_blueDress()


def option_blackDress():
    print("Gorgeous......... and bougi ;) We'll be more weary about our next purchases to be better at saving.")
    time.sleep(1)
    pay()

    print('\n'"How would you like to pay?")
    time.sleep(1)
    print("  a. Debit Card")
    print("  b. Credit Card")
    choice = input(">>> ")

    global credit_avail
    global credit_balance
    global chequings_acc
    global reward_pts
    credit_avail = 500

    if choice.lower() in answer_A:
        chequings_acc -= 70
        afternoon3()

    elif choice.lower() in answer_B:
        credit_avail -= 70
        credit_balance += 70
        reward_pts += 70
        afternoon3()
    else:
        print("Invalid input!")
        time.sleep(0.5)
        option_blackDress()


def afternoon3():
    print("-" * 80)
    print(
        "As you and your friends leave the mall, you pass by other shops and see new headphones on sale at The Source on your right.")
    print(
        "On your left, you see some heels in the showroom to go with your new dress for the dance that are prettier than the ones you have at home, but they do match.")
    time.sleep(2)
    print("Sony Headphones -- $50")
    print("High-heels -- $30")
    print()

    print(
        "You still have a lot of money left on your credit card and a bit more time to spend before you need to be home.")
    time.sleep(1)

    print("How would you like to pay?")
    time.sleep(1)
    print("  a. Take advantage of the deal and purchase the headphones")
    time.sleep(1.5)
    print("  b. Be a showstopper at the dance with those new shoes.")
    time.sleep(1.5)
    print("  c. Buy neither and keep walking.")
    time.sleep(1.5)
    choice = input(">>> ")

    if choice.lower() in answer_A:
        headphones()
    elif choice.lower() in answer_B:
        shoes()
    elif choice.lower() in answer_C:
        neither()
    else:
        print("Invalid input!")
        time.sleep(0.5)
        afternoon3()


def headphones():
    print(
        "Exciting purchase! However this was an IMPULSE purchase. You didn't intend to come to the mall to get headphones.")
    print(
        "It impulsively felt like you saved money when buying them because they were on sale, but you are rather spending more for an item you don't even need and would have saved that money buy not buying it at all.")
    time.sleep(3)
    print()
    print(
        "Being aware of impulsive shopping and compulsive shopping will guide you to make better financial habits everyday.")
    time.sleep(1)

    global credit_avail
    global credit_balance
    global reward_pts

    credit_avail -= 50
    credit_balance += 50
    reward_pts += 50

    print("The purchase went to your credit card. Here are your stats: ")
    time.sleep(1)
    reminderCredit()


def shoes():
    print("Outfit all complete! However this was an IMPULSE purchase.")
    print("You didn't intend to come to the mall to get new shoes and you already had a pair at home.")
    time.sleep(2)
    print("That money would have been better used to pay off your credit card balance later on.")
    print(
        "Being aware of impulsive shopping and compulsive shopping will guide you to make better financial habits everyday.")
    time.sleep(2)

    global credit_balance
    global credit_avail
    global reward_pts

    credit_avail -= 20
    credit_balance += 20
    reward_pts += 20

    print("The purchase went to your credit card. Here are your stats: ")
    time.sleep(1)
    reminderCredit()


def neither():
    print(
        "Excellent decision! You avoided making impulsive purchases and are leaving the mall with exactly what you came for.")
    print("You are developing great financial habits!")
    time.sleep(2)
    print()
    print("Here are your stats:")
    time.sleep(2)
    reminderCredit()


def reminderCredit():
    global credit_balance
    if credit_balance != 0:
        print()
        print(
            "As your credit balance is more than 0, make sure you pay off your credit card within the first 21 days of your purchase to make sure you are not charged any interest.")
        print(
            "After this grace period, you will be charged interest which will make the payments harder to pay off."'\n')
        time.sleep(2)
        print("-" * 80)
        morningSummary()
    else:
        print(
            "You are in a good position with your Credit! If you do use it later on, try to pay it off within the first 21 days to avoid interest payments and maintain a good credit score.")
        print("This will help you for years to come."'\n')
        time.sleep(2)
        print("-" * 80)
        morningSummary()


## Night ##
required = "\nUse only a, b, or c\n"  # Cutting down on duplication


# The story is broken into sections, starting with "intro"
def night():
    print("-" * 80)
    print("""It was a long day at school. You're hungry. You want a snack.""")
    print("You head to your kitchen.")
    print()
    time.sleep(2)
    print("What should you have?")
    time.sleep(1)
    print("  a. A homemade chocolate chip cookie! It is the love of your life!")
    time.sleep(1)
    print("  b. A bowl of frozen grapes. A little weird, but it tastes like candy!")
    time.sleep(1)
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print("Excellent choice! It was delicious!")
        time.sleep(0.5)
        night_2()
    elif choice in answer_B:
        print("Yessss frozen grapes! ")
        time.sleep(0.5)
        night_2()
    else:
        print(required)
        time.sleep(1)
        night()


# next action is
def night_2():
    print("-" * 80)
    print("You have some time to kill before dinner. You finished up your homework at school.")
    print(
        "You decide to watch some TV. You're torn between watching Victorious or iCarly and you only have time for two episodes.")
    print()
    time.sleep(2)
    print("You realize that you can use a financial term called Opportunity Cost to decide.")
    print()
    print("Opportunity Cost is the loss of potential gain from other alternatives when one alternative is chosen.")
    print()
    time.sleep(2)
    print(
        " For example, if you only watch Victorious, the opportunity cost is two episodes of iCarly, since you would be missing out on watching two episodes of iCarly")
    print(" For example, if you only pick iCarly, the opportunity cost is two episodes of Victorious.")
    print()
    time.sleep(2)
    print("What should you do?")
    time.sleep(1)
    print("  a. Watch two episodes of Victorious")
    time.sleep(1)
    print("  b. Watch two episodes of iCarly")
    time.sleep(1)
    print("  c. Watch one episode of iCarly and one episode of Victorious")
    time.sleep(1)

    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print("Great choice! You spend time singing along to the songs!")
        print("Your sister Jane even comes and sings along")
        time.sleep(2)
        night_3()
    elif choice in answer_B:
        print("Awesome choice! iCarly is showing that episode where her room is redone!")
        print("You spend time singing along to the songs and your sister Jane even comes to watch!")
        time.sleep(2)
        night_3()
    elif choice in answer_C:
        print("Awesome choice! iCarly is showing that episode where her room is redone")
        print("Victorious even shows your favourite episode!")
        time.sleep(2)
        night_3()
    else:
        print(required)
        night_2()


# night 3 action
def night_3():
    print()
    print("-" * 80)
    print("It's dinnertime. You leave the TV room, but forget to turn off the lights.")
    print("You're almost at the dinner table, but you can go back and turn off the lights.")
    print()
    time.sleep(2)
    print("What will you do?")
    time.sleep(0.5)
    print("  a. Go back and turn off the lights.")
    time.sleep(1)
    print("  b. Ignore the lights and go have dinner.")
    time.sleep(1)
    choice = input(">>> ")  # input of the choice
    global green_points
    if choice in answer_A:
        print(
            """Awesome choice! Turning off the lights is one of the small decisions that helps the environment every day!""")
        print("""You get one green point!""")
        time.sleep(2)
        green_points = green_points + 1
        night_4()
    elif choice in answer_B:
        print(
            """The lights shine through the door of the TV room. Your sister Jane notices and goes to turn them off.""")
        print("""You should have turned them off earlier. You lose one green point.""")
        time.sleep(2)
        green_points = green_points - 1
        night_4()
    else:
        print(required)
        time.sleep(1)
        night_3()


# night 4 action
def night_4():
    print("-" * 80)
    print("It's getting late. You're about to head to bed, but your sister Jane stops you in the corridor.")
    print("She's talking about how she wants to get the ps5 again.This is the only topic on her mind these days. ")
    print()
    time.sleep(2)
    print(
        "Your mom gave you each some Christmas money to buy things, but Jane doesn't have enough for the ps5 yet and you're in charge on the finances")
    print()
    time.sleep(1)
    print("Her birthday's coming up, so she'll probably have enough soon. Her tone changes. ")
    print()
    time.sleep(1)
    print("I really want to get the WII as well. Could I buy that tonight? What should you do?")
    time.sleep(1)
    print("  a. You remind Jane of her long term goal of getting the ps5 and tell her to hold off on getting the WII. ")
    time.sleep(2)
    print(
        "  b. You cave and tell her to get the WII. She probably won't be able to buy the ps5 later on, but who cares about her long term goal? ")
    time.sleep(2)
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print(
            "Great Choice! Jane remembers how much she wants the ps5 and agrees that she should save up instead."
        )
        time.sleep(1.5)
        night_5()
    elif choice in answer_B:
        print(
            """You begin the process of buying the WII online. Once bought, Jane remembers how much she wanted the ps5 and regrets the WII decision.""")
        print(
            """Jane realizes that she completely forgot her longterm goal and is a little disappointed, but she's okay with getting the WII in the end.""")
        time.sleep(2)
        night_5()
    else:
        print(required)
        time.sleep(0.5)
        night_4()


# night 5 action
def night_5():
    print()
    print("-" * 80)
    print(
        """You've finally made it to bed. You lay down under the covers and notice that you're feeling a little cold.""")
    print("""BURRRRRR. It's not winter-level cold, but it's going to bother you.""")
    print()
    time.sleep(2)
    print("""You decide to do something about it, since you know that you can't sleep when it's cold.""")
    print()
    time.sleep(1)
    print("""What do you do?""")
    time.sleep(1)
    print("  a. Grab a warm blanket from the linen closet.")
    time.sleep(1)
    print("  b. Change into your favourite warm pjs.")
    time.sleep(1)
    print("  c. Turn up the heat.")
    time.sleep(1)

    global green_points
    choice = input(">>> ")  # input of the choice
    if choice in answer_A:
        print("Good choice! You begin to feel warm and can finally sleep! ")
        print(
            "By using less heat, you're helping the environment. You get one green point!"
        )
        time.sleep(2)
        green_points = green_points + 1
        end_of_night()
    elif choice in answer_B:
        print("YESSS!! warmth finally. It feels so good to be in your favourite pjs.")
        print(
            "By not turning up the heat and wearing your pjs, you're helping the enviroment. Here's a green point!"
        )
        time.sleep(2)
        green_points = green_points + 1
        end_of_night()
    elif choice in answer_C:
        print("You can feel the heat instantly. ")
        print(
            "You knew you probably didn't need to turn on the heat, since it wasn't too cold. You lose one green point."
        )
        time.sleep(2)
        green_points = green_points - 1
        end_of_night()
    else:
        print(required)
        night_5()


def end_of_night():
    print('\n'"You finally fall asleep.")
    time.sleep(1)
    print("-" * 80)
    print("-" * 80)
    time.sleep(1)
    print('\n'"The first day is done")
    time.sleep(1)
    print("Chequing Account Balance: ", float(chequings_acc))
    time.sleep(1.5)
    print("Savings Account Balance: ", float(savings_acc))
    time.sleep(1.5)
    print("Green Points Collected: ", float(green_points))
    time.sleep(1.5)


def one_month_later():
    global savings_acc
    savings_acc = interestformula(savings_acc, float(0.05), (1 / 12))
    print("-" * 80)
    print("-" * 80)
    time.sleep(2)
    print('\n'"If you continue your actions for a month. Your account would look like...")
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    temp_green_points = green_points * 30 * 1
    print("Green Points Collected: ", float(temp_green_points))


def six_months_later():
    global savings_acc
    savings_acc = interestformula(savings_acc, float(0.01), (6 / 12))
    print("-" * 80)
    time.sleep(2)
    print('\n'"If you continue your actions for six months. Your account would look like...")
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    temp_green_points = green_points * 30 * 6
    print("Green Points Collected: ", float(temp_green_points))


def one_year_later():
    global savings_acc
    savings_acc = interestformula(savings_acc, float(0.01), (6 / 12))
    print("-" * 80)
    time.sleep(2)
    print('\n'"If you continue your actions for a year. Your account would look like...")
    print("Chequing Account Balance: ", float(chequings_acc))
    print("Savings Account Balance: ", float(savings_acc))
    temp_green_points = green_points * 30 * 12
    print("Green Points Collected: ", float(temp_green_points))


def interestformula(given_money, interest, time):
    temp = given_money
    inner_equation = 1 + (time / 12)
    exponent = (12 * time)
    current_money = inner_equation ** exponent
    current_money = temp * current_money
    return current_money


main()