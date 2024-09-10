master_pass = input("Please Enter the Master Password: ")
def add():
    name = input("Enter the Name: ")
    pwd = input("Enter the Password: ")

    with open('password.txt' , 'a') as f:
        f.write(name + "|" + pwd + "\n")
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", passw)


while True:
    mode = input("Do you want to add a new username & password or view them or do you wan to quit? ").lower()
    if mode == 'q':
        quit()

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Goodbye!")

