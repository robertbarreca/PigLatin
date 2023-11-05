# Pig Latin Translator

This simple Python program translates English text to Pig Latin. It includes a command-line interface for user input and a set of test cases to ensure its functionality.
Usage

To use the Pig Latin Translator, follow these steps:

    Clone or download the repository.
    Make sure you have Python installed on your system.
    Run the program by executing the main.py script in your terminal or preferred Python IDE.

The program will prompt you to enter some English text, and it will then provide the Pig Latin translation.
## Files
main.py

The main.py file contains the main functionality of the Pig Latin Translator. It includes the following functions:

    main(): This function asks the user to input a string, parses it, and calls the to_pig_latin function on each word. It then concatenates the translated words and prints the Pig Latin translation of the input.

    to_pig_latin(word): This function takes a word as input and converts it to Pig Latin. It handles various cases, including words starting with consonants, vowels, and words containing punctuation.

    to_pig_latin_uc(word): This function converts words that begin with an uppercase letter to Pig Latin.

    is_vowel(char): A helper function that checks if a given character is a vowel.

    is_number(num): A helper function that checks if a given string is a number.

    get_punctuation(word): A helper function that separates punctuation from the word and returns them as separate entities.

test_main.py

The test_main.py file contains unit tests for the functions in main.py. It uses the unittest framework to validate the functionality of the Pig Latin Translator.
