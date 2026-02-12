# Write your solution here
def everything_reversed(my_list: list):
    reversed_list = my_list[::-1]
    result = []
    for i in reversed_list:
        result.append(i[::-1])
    return result
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)