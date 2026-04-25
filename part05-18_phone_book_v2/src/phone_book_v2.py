# Write your solution here
def add(persons):
    name = input("name:")
    number = input("number: ")
    persons[name] = number
    print("ok!")

def search(persons):
    name = input("name:")
    for key in persons:
        if name in persons:        
            print(persons[key])
        else:
            print("no number")

def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")

main()
