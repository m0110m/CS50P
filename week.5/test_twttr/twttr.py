def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(phrase):
    for c in phrase:
    if c in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
        phrase = phrase.replace(c, "")
    return phrase


if __name__ == "__main__":
    main()
