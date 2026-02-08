# Write your solution here
list = []

while True:
    new_item = int(input("New item:"))
    if new_item == 0:
        break    
    list.append(new_item)
    in_order = sorted(list)
    print("The list now:", list)
    print("The list in order:", in_order)
print("Bye!")   