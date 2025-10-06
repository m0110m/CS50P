phrase = input("Input: ")
for c in phrase:
    if c in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
        phrase = phrase.replace(c, "")
print(f"Output: {phrase}")
