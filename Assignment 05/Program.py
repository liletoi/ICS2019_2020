import random

def hiLo(number):	
	guess = int(input("Guess a number between 1 and 100: "))
	if guess == number:
		print("Correct! \n")
		answer = input("Do you want to play a game? ")
		number = random.randint(1, 100)
		print(number)
		if answer == "no" or answer == "n" or answer == "No":
			print("Okay!")
			return
	elif guess > number:
		print("Too high!")
	elif guess < number:
		print("Too low!")
	hiLo(number)
	
answer = input("Do you want to play a game? ")

if answer == "no" or answer == "n" or answer == "No":
	print("Okay!")

elif answer == "yes" or answer == "y" or answer == "Yes":
	number = random.randint(1, 100)
	print(number)
	hiLo(number)
