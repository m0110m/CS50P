phrase = input("camelCase: ")
for c in phrase:
    if c.isupper():
        phrase = phrase.replace(c, f"_{c}")
print(f"snake_case: {phrase.lower()}")
