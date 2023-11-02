import unittest
import main

class TestPigLatinTranslator(unittest.TestCase):

    def test_consonantLC(self):
        """
        test_consonantLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case consonant
        """
        result = main.to_pig_latin("hello")
        self.assertEqual(result, "ellohay")

    def test_vowelLC(self):
        """
        test_vowelLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case vowel
        """
        result = main.to_pig_latin("ionic")
        self.assertEqual(result, "ionicay") 

    def test_consonantUC(self):
        """
        test_consonantLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case consonant
        """
        result = main.to_pig_latin("Psychedelic")
        self.assertEqual(result, "Edelicpsychay")

    def test_vowelUC(self):
        """
        test_vowelLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case vowel
        """
        result = main.to_pig_latin("Aardvark")
        self.assertEqual(result, "Aardvarkay") 
    




