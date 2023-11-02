def main():
    print("please enter a word")
    text = input()
    retVal = ""
    for word in text.split(" "):
        # user does not input a word
        if(word.strip == " "):
            continue
        # word contains punctuation
        if(word[-1] == '.' or word[-1] == ';' or word[-1] == ':' or word[-1] == ',' or word[-1] == '?' or word[-1] == '!'):
            retVal += toPigLatin(word[0:-1]) + word[-1] + " "
        # word does not contain punctuation
        else:
            retVal += toPigLatin(word) + " "
    retVal.lower()
    print(retVal)


def toPigLatin(word):
    # first letter is upper case
    if (word[0].isupper()):
        return toPigLatinUC(word)

    # word starts with a vowel
    if (word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u'):
        return word + "ay"
    # word starts with a consonant
    else:
        i = 0
        ending = ""
        for char in word:
            if (char != 'a' and char != 'e' and char != 'i' and char != 'o' or word[0] == 'u'):
                ending += char
                i += 1
            else:
                break
    
        return word[i:] + ending + "ay"
    

def toPigLatinUC(word):
    # word starts with a vowel
    if (word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] =='U'):
        return word + "ay"
    # word starts with a consonant
    else:
        i = 0
        ending = ""
        for char in word:
            #letter is a consonant add to ending
            if (char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u'):
                ending += char.lower()
                i += 1
            else:
                break
    
        return word[i].upper() + word[i+1:] + ending + "ay"
    


if __name__ == '__main__':
    main()
