import random

a=["r","p","s"]



b = input(" Rock (r) . Paper (p) . Scissors (s) : ")
print("You have chosen : ")
if b == "p":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif b == "s":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
elif b == "r" :
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
else :
    print("type in from the given options ")
    exit()

random_value= random.choice(a)
print( " I have chosen : ")
if random_value == "r":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif random_value == "p":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif random_value == "s":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


if b == "r" :
    if random_value == "r":
        print("Drawn")
    elif random_value == "p":
        print(("i win"))
    elif random_value == "s":
        print("you win")
if b == "p" :
    if random_value == "p":
        print("Drawn")
    elif random_value == "s":
        print(("i win"))
    elif random_value == "r":
        print("you win")
if b == "s" :
    if random_value == "s":
        print("Drawn")
    elif random_value == "p":
        print(("you win"))
    elif random_value == "r":
        print("i win")