def main():
    print("please enter a word")
    text = input()
    retVal = ""
    for word in text.split(" "):
        retVal += toPigLatin(word) + " "
    retVal.lower()
    print(retVal)


def toPigLatin(word):
    if (word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'u'):
        return word + "yay"
    else:
        i = 0
        ending = ""
        for char in word:
            if (char != 'a' and char != 'e' and char != 'i' and char != 'u'):
                ending += char
                i += 1
            else:
                break
        return word[i:] + ending + "yay"


if __name__ == '__main__':
    main()
