# requires a few modules

import time
import os
from colorama import Fore, init 

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
print("Unboxing varibles...")
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


## dictionary of the menu and prices 

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

print(open_banner)

print()
print()

# checks if the player wants to enter the store and agrees to the terms

goinside = input("Would you like to view our store? (yes/no) ")

if goinside.strip().lower() == "no":
    print("Thanks for visiting!")
    raise SystemExit

elif goinside.strip().lower() == "yes":
    print()
    print("🛈 ~ Delivery up to 3.5 miles ~ VAT & delivery costs apply ~ Enjoy our food ~ 🛈")
    print()

    agree = input("Do you agree? (yes/no) ")

    if agree.strip().lower() == "yes":
        os.system("cls")

    else:
        print(Fore.RED + "You must agree to continue.")
        raise SystemExit

else:
    print(Fore.RED + "Invalid answer!")
    raise SystemExit


print(open_banner)

print()
print()

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

"""

slow_print(menu, 0.3) # this is my slow print sequence you can run this in thonny to see what it looks like

# planning to add way more like order system way to earn money but still learning