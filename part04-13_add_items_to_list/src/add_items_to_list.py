# Write your solution here
#number items to be added
#individual item to be added
#show the list
items = []
i = 1
number_of_items = int(input('How many items:'))
while i <= number_of_items:
    item = int(input(f"Item {i}:"))
    items.append(item)
    i += 1
print(items)