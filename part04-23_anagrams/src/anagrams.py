# Write your solution here
def anagrams(word1: str, word2: str):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    if sorted_word1 == sorted_word2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("tame", "meta"))