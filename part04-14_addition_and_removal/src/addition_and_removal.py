# Write your solution here
list = []
while True:
    print("The list is now", list)        
    command = input('a(d)d, (r)emove or e(x)it:')
    last_index = len(list)
    if command == "d":        
        list.append(last_index + 1)        
    if command == "r":
        list.remove(last_index)        
    if command == "x":
        print("Bye!")
        break