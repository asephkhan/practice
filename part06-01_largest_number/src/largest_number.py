# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest_number = 0
        for line in new_file.readlines():
            line = line.strip()
            line = int(line)
            if line > largest_number:
                largest_number = line
        return largest_number

if __name__ == "__main__":
    largest_number = largest()
    print(largest_number)
    

