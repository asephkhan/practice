# Write your solution here
def create_tuple(x: int, y: int, z: int):
    my_tuple = (x,y,z)
    first_occurance = min(my_tuple)
    second_occurance = max(my_tuple)
    third_occurance = x + y + z
    result = (first_occurance, second_occurance, third_occurance)
    return result

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
    print(create_tuple(1, 4, 7))


