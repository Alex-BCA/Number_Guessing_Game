import random
print("**Number guessing game**")
number=random.randint(1,100)
print("You have 7 chances!")
chance=7
attempts=0
while True:
    guess=int(input("Enter your guessing number:"))
    attempts+=1
    chance-=1
    if guess==number:
        print("Correct answer!")
        print("You found in",attempts,"attempts")
        print("The correct number was",number)
        break
    else:
        print("Wrong answer!")
        print("Remaining Chance",chance)
    if chance==0:
        print("You have",chance,"chance")
        print("Game over!")
        print("The correct answer was",number)
        break
    print("I Give One Clue:")
    diff=abs(number-guess)
    if diff<=10:
        print("Your guess is very close!")
    elif diff<=20:
        print("Your guess is close!")
    else:
        print("Far away!")
