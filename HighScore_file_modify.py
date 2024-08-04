import random

def game():
    print("You're playing the game... HAhahahaHAHAHaha")
    score = random.randint(1,50)
    
    with open("highScore.txt") as f:
        hscore = f.read()
        if(hscore != ""):
            hscore = int(hscore)
        else:
            hscore = 0
            
    print(f"Your score: {score}")
    
    if(score>hscore):
        with open("demo.txt", "w") as f:
            f.write(str(score))
        
    return score

game()