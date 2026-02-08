# Write your solution here

sentence = []
while True:
    word = input("Word:")
    if word in sentence:
        print(f"You typed in {len(sentence)} different words")
        break
    sentence.append(word)


