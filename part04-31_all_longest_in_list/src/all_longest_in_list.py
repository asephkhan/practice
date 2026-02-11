# Write your solution here
def length_of_longest(my_list: list):
    longest_string = 0
    for i in my_list:
        if len(i) > longest_string:
            longest_string = len(i)
    return longest_string

def all_the_longest(my_list: list):
    max_length = length_of_longest(my_list)
    result = []
    for i in my_list:
        if len(i) == max_length:
            result.append(i)

    return result

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)

#result = all_the_longest(my_list)
#print(result) # ['dorothy', 'richard']