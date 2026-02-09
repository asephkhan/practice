# Write your solution here
def palindromes(word: str):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word    
    if word == reversed_word:
        return True        
    else:
        return False

while True:
    word = input("Please type in a palindrome:")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
