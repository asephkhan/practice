# Copy here code of line function from previous exercise
def line(num, char ):
    if (char == ""):
        char = "*"
    print(num * char[0])
def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1
    # You should call function line here with proper parameters

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(3, "*")