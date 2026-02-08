# Write your solution here
def line(num, char ):
    if (char == ""):
        char = "*"
    print(num * char[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "")