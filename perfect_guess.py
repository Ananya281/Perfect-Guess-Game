import random

randno=random.randint(1,100)
print(randno)

i=0
guess=0
while(guess!=randno):
    guess=int(input("Guess the no. please: "))
    if guess>randno:
        print("Lower no. please")
    elif guess<randno:
        print("Higher no. please")
    i=i+1
if(guess==randno):
    print("Perfect guess!")
    print("You are taken",i,"chance to guess the no.")    
with open("highscore.txt","r") as f:
    highscore=int(f.read())
if(i<highscore):
    print("You have just broken the high score, Congrats!")
    with open("highscore.txt","w") as f:
        f.write(str(i))

