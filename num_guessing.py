import random 
import time 

won = 0
number = random.randint(1,20)

print("Welcome to the number guessing game !!!")

time.sleep(1)
name = input("Enter your name :- ")

time.sleep(1)
print(f"Hello {name}!")

time.sleep(1)
print(f"You will get three chances to guess the correct number.")

time.sleep(1)
for i in range(3):
    guess = int(input("Enter the number :- "))
    if guess < number :
        print('Your guess was too lower !!!!')
    elif guess > number :
        print('Your guess was too higher !!!')
    elif guess == number :
        won += 1
        print('You won the game !!!!')
        break
    
if won != 1:
    print(f'You were too Close. The number was {number}')
