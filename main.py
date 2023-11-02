def main():
    """
    main asks the user to input a string, then parses that string and calls the toPigLatin function on every word in the string. 
    It additionally makes sure all the punctuation is correct based on user input. Finally it then concatenates all the returned
    words from the toPigLatin() and prints the pig latin translation of the user input
    """ 
    print("please enter some english")
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
    """
    toPigLatin takes in a word and first checks to see if the first letter is capital, if it is is then passes it to toPigLatinUC().
    Otherwise it converts the word to pig latin itself

    :param word: the word to be converted to pig latin
    :return: the pig latin translation of the word argument
    """
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
    """
    toPigLatinUC converts a word that begins with an upper case letter to pig latin.

    :param word: the word to be converted to pig latin
    :return: the pig latin translation of the word argument
    """
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
