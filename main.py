def main():
    """
    main asks the user to input a string, then parses that string and calls the toPigLatin function on every word in the string. 
    It then concatenates all the returned words from the toPigLatin() and prints the pig latin translation of the user input
    """
    print("please enter some english")
    text = input()
    retVal = ""
    for word in text.split(" "):
        # user does not input a word
        if not word.strip():
            continue
        retVal += to_pig_latin(word) + " "
    retVal.lower()
    print(retVal)


def to_pig_latin(word):
    """
    to_pig_latin takes in a word and first checks to see if the first letter is capital, if it is is then passes it to toPigLatinUC().
    Otherwise it converts the word to pig latin itself

    :param word: the word to be converted to pig latin
    :return: the pig latin translation of the word parameter
    """

    if (is_number(word)):
        return word

    # first letter is upper case
    if (word[0].isupper() and not is_vowel(word[0])):
        return to_pig_latin_uc(word)

    punctuation = ""
    containsPunctuation = False

    # Check if word contains punctuation
    for char in reversed(word):
        if char in ".;:,?!":
            punctuation = char + punctuation
            containsPunctuation = True
        else:
            break

    word = word[:len(word) - len(punctuation)]

    # word starts with a vowel
    if (is_vowel(word[0])):
        # word contains punctuation add it back
        if containsPunctuation:
            return word + "ay" + punctuation
        # word does not contain punctuation
        else:
            return word + "ay"
    # word starts with a consonant
    else:
        i = 0
        ending = ""
        for char in word:
            if (not is_vowel(char)):
                ending += char
                i += 1
            else:
                break
        # word contains punctuation add it back
        if containsPunctuation:
            return word[i:] + ending + "ay" + punctuation
        # word does not contain punctuation
        else:
            return word[i:] + ending + "ay"


def to_pig_latin_uc(word):
    """
    to_pig_latin_uc converts a word that begins with an upper case letter to pig latin.

    :param word: the word to be converted to pig latin
    :return: the pig latin translation of the word parameter
    """
    punctuation = ""
    containsPunctuation = False

    # no english words are a one letter consonant
    if (len(word) == 1):
        return ""

    # Check if word contains punctuation
    for char in reversed(word):
        if char in ".;:,?!":
            punctuation = char + punctuation
            containsPunctuation = True
        else:
            break

    word = word[:len(word) - len(punctuation)]

    i = 0
    ending = ""
    for char in word:
        # letter is a consonant add to ending
        if (not is_vowel(char)):
            ending += char.lower()
            i += 1
        else:
            break
    if (containsPunctuation):
        return word[i].upper() + word[i+1:] + ending + "ay" + punctuation
    else:
        return word[i].upper() + word[i+1:] + ending + "ay"


def is_vowel(char):
    """
    is_vowel is a helper method that just check if a given character is a vowel

    :param char: the character that is checked if it is a vowel
    :return: true if the character is a vowel and false otherwise
    """
    vowels = "aeiouAEIOU"
    return char in vowels


def is_number(num):
    """
    is_number is a helper method that checks whether a given string is a number or not

    :param num: the string to be checked if it is number or not
    :return: true if the string is anumber and false otherwise
    """
    try:
        float(num)  # Try to convert the string to a float
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
