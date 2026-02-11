# Write your solution here
def length_of_longest(my_list: list):
    longest_string = 0
    for i in my_list:
        if len(i) > longest_string:
            longest_string = len(i)
    return longest_string

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
#    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
