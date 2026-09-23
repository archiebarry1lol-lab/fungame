# rest.py
# requires a few modules

import time
import os
from colorama import Fore, init

checkout_banner = """
+======================================+
|                                      |
|          LA COSTA CHECKOUT           |
|        --------------------          |
|                                      |
+======================================+
"""

outside_banner = """
        ========================================
            =============================
                        TOWN
            =============================
        ========================================
"""
menu_items = {
    1: {"name": "Large Cheese Burger Meal", "price": 12.99},
    2: {"name": "Peri Chicken Meal", "price": 16.99},
    3: {"name": "Supreme Tacos Meal", "price": 11.39},
    4: {"name": "Cheesy Garlic Bread", "price": 4.89},
    5: {"name": "Peri Peri Fries", "price": 3.39},
    6: {"name": "Garlic Mushrooms", "price": 3.39},
    7: {"name": "Sex On The Beach", "price": 13.50},
    8: {"name": "Bakewell Sour", "price": 12.95},
    9: {"name": "Hot Honey Bee", "price": 11.39},
    10: {"name": "Soft Drink", "price": 1.33},
    11: {"name": "Milkshake", "price": 3.39},
    12: {"name": "Beer Draught", "price": 4.39},
    13: {"name": "Green Tea", "price": 2.29},
    14: {"name": "English Tea", "price": 3.29},
    15: {"name": "Espresso Shots", "price": 4.29},
    16: {"name": "Brownie Cake & Gelato", "price": 4.89},
    17: {"name": "Chocolate Cookies & Gelato", "price": 6.30},
    18: {"name": "Volcano Cake & Gelato", "price": 4.89}
}

open_banner = f"""
{Fore.YELLOW}                 ====================
                  ==== La Costa ====
                 ====================
                     ===========
{Fore.GREEN}                     == OPEN! ==
{Fore.YELLOW}                     ===========
"""

# 2 banners 1 for closed one for open will be used in future also has nice indentation to look central inside a shell

closed_banner = f"""
{Fore.YELLOW}                 ====================
                  ==== La Costa ====
                 ====================
                     =============
{Fore.RED}                     == CLOSED! ==
{Fore.YELLOW}                     =============
"""

mini_menu = """
========== LA COSTA MENU ==========

[1] Cheese Burger Meal       $12.99
[2] Peri Chicken Meal        $16.99
[3] Supreme Tacos Meal       $11.39

[4] Cheesy Garlic Bread       $4.89
[5] Peri Peri Fries           $3.39
[6] Garlic Mushrooms           $3.39

[7] Sex On The Beach         $13.50
[8] Bakewell Sour            $12.95
[9] Hot Honey Bee            $11.39

[10] Soft Drink               $1.33
[11] Milkshake                $3.39
[12] Beer Draught             $4.39

[13] Green Tea                $2.29
[14] English Tea              $3.29
[15] Espresso Shots           $4.29

[16] Brownie Cake & Gelato    $4.89
[17] Cookies & Gelato         $6.30
[18] Volcano Cake & Gelato    $4.89

[-] Return to Town
===================================
"""

menu = """
                  ====    MENU    ====

== Sides & Starters ==                   == Burgers & Proteins ==

[4] Cheesy Garlic Bread ~ $4.89          [1] Large Cheese Burger Meal ~ $12.99
[5] Peri Peri Fries ~ $3.39              [2] Large Peri Chicken & 2 Sides Meal ~ $16.99
[6] Garlic Mushrooms ~ $3.39             [3] Supreme Tacos & 2 Sides Meal ~ $11.39


                  ====    DRINKS    ====

== Soft Drinks & Milkshakes ==           == Cocktails ==

[10] Any Soft Drink ~ $1.33              [7] Sex On The Beach ~ $13.50
[11] Any Milkshake ~ $3.39               [8] Bakewell Sour ~ $12.95
[12] Beer Draught ~ $4.39                [9] Hot Honey Bee ~ $11.39


                  ====    AFTERS    ====

== Desserts & Sweet Treats ==            == Tea & Coffee ==

[16] Brownie Cake & Gelato ~ $4.89       [13] Green Tea ~ $2.29
[17] Chocolate Cookies & Gelato ~ $6.30  [14] English Tea ~ $3.29
[18] Volcano Cake & Gelato ~ $4.89       [15] Espresso Shots ~ $4.29

[-] Return to Town
"""

def visit_lacosta():
    os.system("cls")

    print(open_banner)
    b()
    b()

    goinside = input("Would you like to view our store? (yes/no/- to return) ")

    if goinside == "-":
        return

    if goinside.strip().lower() == "no":
        print("Thanks for visiting!")
        input("Press Enter to return...")
        return

    elif goinside.strip().lower() == "yes":
        print()
        print("🛈 ~ VAT & taxes apply ~ Enjoy our food ~ 🛈")
        print()

        agree = input("Do you agree? (yes/no/- to return) ")

        if agree == "-":
            return

        if agree.strip().lower() == "yes":
            os.system("cls")
            print(open_banner)
            b()
            slow_print(mini_menu, 0.3)
            b()
            b()
            
            order_choice = input("What would you like to order? [- to return] ")

            if return_check(order_choice):
                return
            
            order_choice = int(order_choice) # it tries to convert their text into an integer so "1" becomes 1 but "hello" would currently crash im gonna add protection
            selected_item = menu_items[order_choice] # [order_choices] uses our dictionary to find the number of the ordered item...
            
            os.system("cls")
            print(checkout_banner)
            
            print(f"Item(s): {selected_item['name']}") # prints the item they selected to buy 
            print(f"Price: ${selected_item['price']:.2f}") # prints the selected items price via our dictionary
            print(f"Balance: ${player['balance']:.2f}") # prints player balance via our player dictionary
            
            

        else:
            print(Fore.RED + "You must agree to continue.")
            input("Press Enter to return...")

    else:
        print(Fore.RED + "Invalid answer!")
        input("Press Enter to return...")

def return_check(answer):
    if answer == "-":
        return True
    return False

# clock and level never refresh on the terminal screen...

def game_clock():
    elapsed = time.time() - game_start_time

    ten_minute_chunks = int(elapsed // 2)
    game_minutes = ten_minute_chunks * 10

    starting_minutes = 8 * 60
    total_minutes = starting_minutes + game_minutes

    hour = (total_minutes // 60) % 24
    minute = total_minutes % 60

    return f"{hour:02d}:{minute:02d}"

def update_level():
    elapsed = time.time() - game_start_time

    total_xp = 50 + int(elapsed // 20) * 50

    player["level"] = 1 + (total_xp // 100)
    player["xp"] = total_xp % 100
    
def hud():
    update_level()
    print(f"Time: {game_clock()} | Level: {player['level']} | XP: {player['xp']}/100")

# js a blank line function learning basics of functions and indentations

def b():
    print()

# slow print definition for printing lines slowly useful for the menu and walking animations etc found online

def slow_print(text, delay=0.08):
    for line in text.splitlines(): # goes through 1 line at a time and not 1 character 'typewriter' effect
        print(line) # prints one line at a time, e.g. "Hello" first, then "World" on the next loop if there different lines
        time.sleep(delay) # the time is customisable example down "slow_print(menu, 0.3)" the 0.3 custom sleep time per line overrides 0.08 the default
        
init(autoreset = True)



# ---------------------------------------------------------------- loading game sequence + main game
# ---------------------------------------------------------------- my python project to help me understand python even more

print(Fore.RED + "                       ARCHIE")
print(Fore.RED + "                       STUDIOS")

print()
print()
print("Loading game interior...")
print()
time.sleep(1)
print("We will never ask for personal information...")
print()
time.sleep(1)
print("Unboxing variables...")
print()
time.sleep(1)
print("Loading messages...")
print()
time.sleep(1)
print()

print()
print()

# gonna use these premade messages in the future for the main game

messages = {
    "invalid": "Invalid order!",
    "completed": "Order completed!",
    "preparing": "Preparing food...",
    "welcome": "Welcome!"
}

print(Fore.RED + messages["invalid"])
print(Fore.GREEN + messages["completed"])
print(Fore.YELLOW + messages["preparing"])
print(messages["welcome"])

print()
print()

print("Loading an original Archie Studios game...")
time.sleep(3)

# below is what clears the terminal before the actual game

os.system("cls")

# jobs you can choose inside the game

job_info = f"""

Job Choices...

[1] Barista ~ $12/hr (Level 1 Required...)
[2] Construction Worker ~ $18/hr (Level 3 Required...)
[3] Doctor ~ $32/hr (Level 5 Required...)
[4] Stay broke... ~ $3/hr (0 Requirements...)

"""

# player data for the main game

player = {
    "name": "",
    "balance": 50.00,
    "job": "Unemployed",
    "level": 1,
    "xp": 50,
}

# asks for players name in game not real name

b()
b()
b()
b()

player["name"] = input("Enter your player name: ")
os.system("cls")

# welcome sequence with balance name etc

def info_banner():
    print(f"Welcome, {player['name']}.")
    print(f"Balance: ${player['balance']:.2f}")
    print(f"Job: {player['job']}.")

b()
b()
b()

info_banner()

print()
print()

input("Press Enter to continue...")
game_start_time = time.time()
os.system("cls")

# MAIN MENU CAN BE RETURNED TO AT ANYTIME WHILE DOING A MINIGAME/SECTOR OF THE GAME

while True:
    os.system("cls")
    hud()
    print(outside_banner)
    b()
    print("[-] Return to Town ~ AT ANY TIME...")
    b()
    b()
    print("[1] Visit La Costa...")
    print("[2] Find a job...")
    print("[3] Player information...")
    print("[4] Quit")
    print("[5] Go to work... [JOB REQUIRED]")
    b()
    choice = input("Pick a number interaction... ")
    
    if choice == "1":
        slow_print("""
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        Walking over to La Costa...
        """,0.2)
        b()
        b()
        visit_lacosta()
    
    elif choice == "2":
        b()
        b()
        job_choice = input("What do you desire to work as? [- to return] ")

        if return_check(job_choice):
            continue
        b()
        # function that allows you to choose a job checks level requirements etc
        
    elif choice == "3":
        b()
        info_banner()
        b()
        b()
        print(job_info)
        input("Press Enter to return...") # returns back to main menu cuz its js an info screen
    
    elif choice == "4":
        raise SystemExit
    
    elif choice == "5":
        # function that grabs the users job and does an animation taking them to the job 'minigame'
    
    else:
        slow_print("""I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.
I cant think that far yet, I am solo developing chill.""", 0.3)
        continue