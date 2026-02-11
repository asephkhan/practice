# Write your solution here
def list_sum(a: list, b: list):
    new_list = []

    for i in range(len(a)):
        new_list.append(a[i] + b[i])
    
    return new_list
        
        
    print("new_list", new_list)
    return new_list
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) 