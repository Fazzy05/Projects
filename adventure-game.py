name = input("Please Enter your name: ")
start_adventure = input(f"Hello " + name + ", You have been chosen for a adventure, would you like to do it or no?(yes/no)").lower()
if start_adventure == 'yes':
    print("Great! You have started your Journey!")
    answer = input("There is a Zombie in your Way. Do you want to kill it or avoid it?(kill/avoid): ")
    if answer == 'kill':
        print("You Killed the Zombie!")
        answer = input("Now, there is a cave ahead do you want to enter? (yes/no)")
        if answer == 'yes':
            print("You Entered a Cave and now there is a door which is locked! ")
            answer = input("Do you have the key?(yes/no) ")
            if answer == 'yes':
                print("How???")
                print("You are a liar!")
                quit()
            else:
                print("You are a loser!")
                quit()
        else:
            print("You are a loser!")
            quit()
    else:
        print("You are a loser!")
        quit()
else:
    print("You are a loser!")
    quit()