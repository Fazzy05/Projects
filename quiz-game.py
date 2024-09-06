print("Hello! Welcome to the Quiz Game!")
play = input("Do you want to play? ")
score = 0
if play.lower() != "yes":
    quit()
print("Yay!!! Lets start the Game!")

question = input("What is the capital of Pakistan? ")
if question.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What is the capital of France? ")
if question.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What is the capital of UK? ")
if question.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What is the capital of Turkey? ")
if question.lower() == "istanbul":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What is the capital of Japan? ")
if question.lower() == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You answered " + str(score) + " Questions Correct!")
print("You Got " + str((score / 5) * 100) + "%.")