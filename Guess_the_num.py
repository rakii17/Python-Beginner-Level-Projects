import random

random_num = random.randint(1, 100)
guessed_num = -1
guesses = 0

while(guessed_num != random_num):
    guessed_num = int(input("Guess the number: "))   
    
    if(guessed_num > random_num):
        print("Try Lower number ")  
        guesses += 1
    elif(guessed_num < random_num):
        print("Try Higher number ")
        guesses += 1
        
print(f"You have guessed the number {random_num} correctly in {guesses} attempt/s")