# Pig Latin Translator

This simple Python program translates English text to Pig Latin. It includes a command-line interface for user input and a set of test cases to ensure its functionality.

## Motivation

I created the Pig Latin Translator for a very personal and heartwarming reason. My little cousin, has always had a fascination with Pig Latin. He would always speak it Pig Latin with his friends, and I was always amazed by his enthusiasm for it.

As someone passionate about coding and technology, I saw an opportunity to introduce him to the world of programming and share in his love for Pig Latin. I decided to create this Pig Latin Translator not only to keep up with his code but also to provide a fun and educational platform for him to explore the world of coding, while learning a new programming language myself.

My motivations for this project are as follows:

1. **Introducing a Young Mind to Coding**: I wanted to nurture my cousin's curiosity and love for language games and coding. By creating a Pig Latin Translator, I aim to make coding fun, accessible, and relatable to a young learner.

2. **Exploring a New Programming Language**: This project gave me the perfect opportunity to dive into Python, a language I had always wanted to learn. I hope that by working on this project, I can foster my own passion for programming and share that enthusiasm with my cousin.

3. **Bringing Joy through Technology**: Ultimately, the goal of this project is to bring joy and learning through technology. I hope that other kids and coding enthusiasts can enjoy the fun of Pig Latin while gaining some insights into the world of programming.

I believe that this project embodies the magic of coding, where a simple language game can create a bridge between generations, introduce a young mind to the wonders of technology, and ignite a love for learning and coding.

## Usage

To use the Pig Latin Translator, follow these steps:

1. Clone or download the repository.
2. Make sure you have Python installed on your system.
3. Run the program by executing the main.py script in your terminal or preferred Python IDE.

The program will prompt you to enter some English text, and it will then provide the Pig Latin translation.

## Files

### main.py

The main.py file contains the main functionality of the Pig Latin Translator. It includes the following functions:

- main(): This function asks the user to input a string, parses it, and calls the to_pig_latin function on each word. It then concatenates the translated words and prints the Pig Latin translation of the input.

- to_pig_latin(word): This function takes a word as input and converts it to Pig Latin. It handles various cases, including words starting with consonants, vowels, and words containing punctuation.

- to_pig_latin_uc(word): This function converts words that begin with an uppercase letter to Pig Latin.

- is_vowel(char): A helper function that checks if a given character is a vowel.

- is_number(num): A helper function that checks if a given string is a number.

- get_punctuation(word): A helper function that separates punctuation from the word and returns them as separate entities.

### test_main.py

The test_main.py file contains unit tests for the functions in main.py. It uses the unittest framework to validate the functionality of the Pig Latin Translator.

## Testing

You can run the unit tests in test_main.py to ensure that the Pig Latin Translator functions correctly. To do this, execute the following command in your terminal:
`python3 -m unittest test_pigLatin.py` This will run the test cases and report any failures or errors.
