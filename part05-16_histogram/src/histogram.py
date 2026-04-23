# Write your solution here

def histogram(string : str):
    dictionary = {}    
    for letter in string:
        if letter in dictionary:
            dictionary[letter] += "*"       
        if letter not in dictionary:
            dictionary[letter] = "*"
    for key, value in dictionary.items():
        print(key, value)
if __name__ == "__main__":
    histogram("hello!")