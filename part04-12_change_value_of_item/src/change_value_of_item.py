# Write your solution here

list = [1,2,3,4,5]


while True:
    index = int(input("INDEX:"))
    if index == -1:
        break
    new_value = int(input("New value:"))
    list[index] = new_value
    print(list)