# Write your solution here
user_input = int(input("command(1 search, 2 add, 3 quit):"))
phonebook = {}


def add():    
    user_name = input("name:")
    user_phone_number = int(input("number:"))
    phonebook[user_name] = user_phone_number
    print("ok!")

def search():
    user_name = input("name:")
    print(phonebook[user_name])

def quit_program():
    print("quitting...")

    if user_input == 1:
        serach()
    if user_input == 2:
        add()
    if user_input == 3:
        quit_program()




   

