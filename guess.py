import random
no=random.randint(1,9)
chance=5

while chance>0:
    guess=int(input("Enter a number "))
    if no==guess:
        print("Congrats")
        break

    elif guess<no :
        print("Your guess is low",guess)
        chance-=1
    elif guess>no:
        print("your guess is high",guess)
        chance-=1
         

if chance==0:
    print("Game Over Correct answer is",no)
