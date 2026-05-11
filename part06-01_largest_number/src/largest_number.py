# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest_number = 0
        for number in new_file.read():
            
            number = number.replace("\n", "")
            number = int(number)
            if number > largest_number:
                largest_number = number
        print(largest_number)

if __name__ == "__main__":
    largest()

