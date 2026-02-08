# Copy here code of line function from previous exercise and use it in your solution
def line(num, char ):
    if (char == ""):
        char = "*"
    print(num * char[0])
def shape(width, char_tri, height_rec, char_rec):
    i = 0
    j = 0
    while i < width:
        i += 1
        line(i, char_tri)

    while j < height_rec:
        line(width, char_rec)
        j += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(6, "x", 4, "o")