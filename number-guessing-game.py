import random

top_range = input("Please Enter a Number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please Enter a Number Above 0 next time!")
        quit()
else:
    print("Please Enter a number next time!")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Please Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a Number next time!")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were Above the Number")
    else:
        print("You were Below the Number")

print("You guessed the Number in", guesses, "guesses")



