import random

def play():
    print("Welcome to Snake, Water, Gun Game")
    print("Select : -1 for Snake, 0 for Water, 1 for Gun")
    
    your_choice = int(input("Enter your choice: "))
    if your_choice not in [-1, 0, 1]:
        print("Invalid selection. Select : -1 for Snake, 0 for Water, 1 for Gun")
        return
    
    system_choice = random.choice([-1, 0, 1])
    print(f"Computer chose: {system_choice}")
    
    if your_choice == system_choice:
        result = ("It's a Tie!")
        
    elif (your_choice == -1 and system_choice == 1) or (your_choice == 1 and system_choice == 0) or (your_choice == 0 and system_choice == -1):
        result = ("Hurray!, You Won...")
        
    else:
        result = ("You Lose....")
        
    print(result)
    
play()