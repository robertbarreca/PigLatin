import unittest
import main

class TestPigLatinTranslator(unittest.TestCase):

    def test_consonantLC(self):
        """
        test_consonantLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case consonant
        """
        self.assertEqual(main.to_pig_latin("hello"), "ellohay")

    def test_vowelLC(self):
        """
        test_vowelLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case vowel
        """

        self.assertEqual(main.to_pig_latin("ionic"), "ionicay") 

    def test_consonantUC(self):
        """
        test_consonantLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case consonant
        """
        self.assertEqual(main.to_pig_latin("Psychedelic"), "Edelicpsychay")

    def test_vowelUC(self):
        """
        test_vowelLC tests the functionality of the toPigLatin function when passed a word that 
        starts with a lower case vowel
        """
        self.assertEqual(main.to_pig_latin("Aardvark"), "Aardvarkay") 
    




