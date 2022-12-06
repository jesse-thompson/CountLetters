userString = input("Please input a string\n")
lettersUsed = {}


def count_letters(inputString):
    for i in inputString:
        if i != " ":
            # if the letter is not found in lettersUsed, it is initialized as 0, else it is incremented
            lettersUsed[i] = lettersUsed.get(i, 0) + 1
    print(lettersUsed)


count_letters(userString)
