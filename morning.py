
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
    print("1. Savings accounts are bank accounts where you store your savings, money you intend to save and not spend.")
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
    credit_avail = 500
    print("Credit Balance: ", int(credit_avail))
    print("Credit Available: ", int(credit_balance))
    print("Reward Points:". int(reward_pts))



def afternoon():
    print( " Now that you've developed ideal basic spending and saving habits, your parents have decided to provide you with your very first Credit Card! ")
    print("""Here is what you should know about Credit:
    1. The money on your credit card is not your money, but the bank's money so it isn't free.
    When you use your Credit Card to make purchases, the bank is letting you borrow some amount of money to spend
    that must be paid back eventually. After the 21 day grace period, the longer it takes you to pay back the balance,
    the balance, the more the interest will add up.

    2. There's a limit to HOW MUCH you can purchase on your credit card.
    It is known as a credit limit ($500 in your case) and is the maximum amount of money you can borrow at a time from 
    the bank. Keeping a low credit card balance makes it easier to pay off and build a better credit history.

    3. You're being graded.
    Everybody who uses a credit card has a credit score which is based on your credit card history (how frequently you 
    make payments, outstanding loans, your available credit etc.) It ranges on average from 300 to 850, with higher
    credit scores being better. 
    Having a good credit score gives you benefits such as approval for loans in the future for a mortgage for a new house
    or buying a new car, better interest rates on your loans and more.""")
    afternoon1()
    global credit_balance


def afternoon1():
    print("""The Spring Homecoming dance is coming up and you don't have a dress for the occasion. Your friends offer you
          some dresses for you to borrow or offer to go to the mall this afternoon so you could buy a brand new one yourself. You choose:
          A. Stick with some existing options for dresses from your kind friends.
          B. Go to the mall with them so you can all purchase a new one for the dance.""")
    choice = input(">>> ")
    if choice.lower() in answer_A:
        option_oldDress()
    elif choice.lower() in answer_B:
        option_newDress()
    else:
        print("Invalid input! Please type yes/no OR y/n")
        afternoon1()


def option_oldDress():
    print("""Great choice! You saved money buy choosing not to buy a new dress and rather borrow one instead.
    Additionally, by not having to travel to the mall, you reduce your carbon emissions by saving your fuel.""")
    green_points += 5
    print("Below are your stats: ")
    morningSummary()
    afternoon2()


def option_newDress():
    print(""" Sounds fun! Although there was a missed opportunity to save money on purchasing a new dress entirely for one day, we can continue
    finding other options to be financially smart! :)""")
    green_points -=2
    morningSummary()
    afternoon2()

def afternoon2():
    print("""You have settled on 3 options that you love:
    
    A. A long red maxi dress at $40.
    B. A blue bell-sleeve dress at $50.
    C. A black off-the-shoulder dress at $70. """)
    choice = input("Which dress do you choose: ")

    if choice.lower() in answer_A:
        option_redDress()
    elif choice.lower() in answer_B:
        option_blueDress()
    elif choice.lower() in answer_C:
        option_blackDress()
    else:
        print("Invalid input!")
        afternoon2()


def pay():
    print("""You can choose to complete this purchase with your debit card or your new credit card.
    Here are some tips to keep in mind.

    Credit: By using a credit card for shopping purchases, you can gain reward points based on each dollar you spent at certain retailers.
    By accumulating points later on, you can redeem them for other purchases without having to spent real money or use it to pay off your credit card.
    However you do have to make sure you pay off the purchase eventually with your own money. If you're unable to do so in time, you will be charged interest.
    -----------------
    Debit: By using your debit card, you are spending your own money and won't have to worry about any remaining payments after the purchase.
    But you may miss out on the opportunity to collect reward points.""")

def option_redDress():
    print("Beautiful choice and economic purchase!")
    pay()
    choice = input(""" How  would you like to pay?
    A. Debit Card
    B. Credit Card""")

    global credit_avail
    global credit_balance
    credit_avail = 500

    if choice.lower() in answer_A:
        chequings_acc -= 40
    elif choice.lower() in answer_B:
        credit_avail -= 40
        credit_balance += 40
        reward_pts += 40
    else:
        print("Invalid input!")
        option_redDress()

def option_blueDress():
    print("Lovely pick at a relatively good price!")
    pay()
    choice = input(""" How  would you like to pay?
    A. Debit Card
    B. Credit Card""")

    global credit_avail
    global credit_balance
    credit_avail = 500

    if choice.lower() in answer_A:
        chequings_acc -= 50
    elif choice.lower() in answer_B:
        credit_avail -= 50
        credit_balance += 50
        reward_pts += 50
    else:
        print("Invalid input!")
        option_blueDress()

def option_blackDress():
    print("Gorgeous......... and bougi ;) We'll be more weary about our next purchases to be better at saving.")
    pay()

    choice = input(""" How  would you like to pay?
    A. Debit Card
    B. Credit Card""")

    global credit_avail
    global credit_balance
    credit_avail = 500

    if choice.lower() in answer_A:
        chequings_acc -= 70

    elif choice.lower() in answer_B:
        credit_avail -= 70
        credit_balance += 70
        reward_pts += 70
    else:
        print("Invalid input!")
        option_blackDress()



def afternoon3():

    print("""As you and your friends leave the mall, you pass by other shops and see new headphones on sale at The Source on your right, and on 
    your left, you see some heels in the showroom to go with your new dress for the dance that are prettier than the ones you have at home, but they do match .
    Sony Headphones -- $50
    High-heels -- $30
    
    You still have a lot of money left on your credit card and a bit more time to spend before you need to be home.
    What would you like to do?""")

    choice = input(""")
    A. Take advantage of the deal and purchase the headphones
    B. Be a showstopper at the dance with those new shoes.
    C. Buy neither and keep walking. """)

    if choice.lower() in answer_A:
        headphones()
    elif choice.lower() in answer_B:
        shoes()
    elif choice.lower(0 in answer_C):
        neither()
    else:
        print("Invalid input!")
        afternoon3()

def headphones():
    print(""" Exciting purchase! However this was an IMPULSE purchase. 
    You didn't intend to come to the mall to get headphones. It impulsively felt like you saved money when buying them because they were on sale
    but you are rather spending more for an item you don't even need and would have saved that money buy not buying it at all.
    Being aware of impulsive shopping and compulsive shopping will guide you to make better financial habits everyday.
    """)
    credit_avail -= 50
    credit_balance += 50
    reward_pts += 50

    print("The purchase went to your credit card. Here are your stats: ")
    morningSummary()
    reminderCredit()

def shoes():
    print(""" Outfit all complete! However this was an IMPULSE purchase.
      You didn't intend to come to the mall to get new shoes and you already had a pair at home.
      That money would have been better used to pay off your credit card balance later on.
    Being aware of impulsive shopping and compulsive shopping will guide you to make better financial habits everyday.""")
    credit_avail -= 20
    credit_balance += 20
    reward_pts += 20

    print("The purchase went to your credit card. Here are your stats: ")
    morningSummary()
    reminderCredit()

def neither():
    print(""" Excellent decision! 
    You avoided making impulsive purchases and are leaving the mall with exactly what you came for. You are developing great financial habits!
    
    Here are your stats: """)
    morningSummary()
    reminderCredit()


def reminderCredit():
    if credit_balance != 0:
        print("""As your credit balance is more than 0, make sure you pay off your credit card within the first 21 days of your purchase
          to make sure you are not charged any interest. After this grace period, you will be charged interest which will make the payments
           harder to pay off.""")
    else:
        print("""You are in a good position with your Credit! If you do use it later on, try to pay it off within the first 21 days to avoid
             interest payments and maintain a good credit score, which will help you for years to come.""")

