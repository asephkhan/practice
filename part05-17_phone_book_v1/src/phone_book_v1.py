# Write your solution here
#user_input = int(input("command(1 search, 2 add, 3 quit):"))
phonebook = {}
def add():    
    user_name = input("name:")
    user_phone_number = input("number:")
    phonebook[user_name] = user_phone_number
    print("ok!")

def search():
    user_name = input("name:")
    if user_name not in phonebook:
        print("no number")
    if user_name in phonebook:
        print(phonebook[user_name])

def quit_program():
    print("quitting...")



while True:
    user_input = int(input("command(1 search, 2 add, 3 quit):"))
    if user_input == 1:
        search()

    elif user_input == 2:
        add()

    elif user_input == 3:
        quit_program()
        break




   

