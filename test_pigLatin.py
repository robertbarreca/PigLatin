import unittest
import main


class TestPigLatinTranslator(unittest.TestCase):

    def test_to_pig_latin_lc(self):
        """
        test_to_pig_lat tests the functionality of the to_pig_latin function 
        """
        # check basic word starts with consonant
        self.assertEqual(main.to_pig_latin("hello"), "ellohay")

        # check positve integer
        self.assertEqual(main.to_pig_latin("15"), "15")

        # check positive float
        self.assertEqual(main.to_pig_latin("3.14"), "3.14")

        # check negative integer
        self.assertEqual(main.to_pig_latin("-36"), "-36")

        # check negative float
        self.assertEqual(main.to_pig_latin("-2.72"), "-2.72")

        # check word that starts with vowel
        self.assertEqual(main.to_pig_latin("ionic"), "ionicay")

        # check word that starts with consonant chunk
        self.assertEqual(main.to_pig_latin("pyramid"), "amidpyray")

        # check word that ends in punctuation
        self.assertEqual(main.to_pig_latin("ruler."), "ulerray.")

        # check word that ends with lots of punctuation
        self.assertEqual(main.to_pig_latin("panda!!!"), "andapay!!!")

        # check sentence
        sentence = "the dog jumped over the fence, ate his kibble, and took a nap."
        words = sentence.split()
        ret_val = ""

        for word in words:
            ret_val += main.to_pig_latin(word) + " "

        self.assertEqual(
            ret_val, "ethay ogday umpedjay overay ethay encefay, ateay ishay ibblekay, anday ooktay aay apnay. ")

    def test_to_pig_latin_uc(self):
        """
        test_consonantLC tests the functionality of the to_pig_latin function when the word contains a word that starts with an upper case letter
        """
        # check word that starts with consonant
        self.assertEqual(main.to_pig_latin("Paper"), "Aperpay")

        # check word that starts with consonant chunk
        self.assertEqual(main.to_pig_latin("Psychedelic"), "Edelicpsychay")

        # check word that starts with a vowel
        self.assertEqual(main.to_pig_latin("Uruguay"), "Uruguayay")

        # check word that has capital in middle of it starting with vowel
        self.assertEqual(main.to_pig_latin("iPod"), "iPoday")

        # check word that has capital in middle of it starting with consonant
        self.assertEqual(main.to_pig_latin("fReeDom"), "eeDomfRay")

    def test_is_vowel(self):
        """
        test_is_vowel tests the functionality of the is_vowel function
        """
        # check lower case vowel
        self.assertTrue(main.is_vowel('i'))

        # check upper case vowel
        self.assertTrue(main.is_vowel('U'))

        # check lower case consonant
        self.assertFalse(main.is_vowel('r'))

        # check upper case consonant
        self.assertFalse(main.is_vowel('K'))

        # check non-letter
        self.assertFalse(main.is_vowel('@'))

        # check number
        self.assertFalse(main.is_vowel('9'))

    def test_is_number(self):
        """
        test_is_number tests the functionality of the is_number function
        """
        # check positive int
        self.assertTrue(main.is_number("194"))

        # check positive float
        self.assertTrue(main.is_number("6.234"))

        # check negative int
        self.assertTrue(main.is_number("-320"))

        # check negative float
        self.assertTrue(main.is_number("-12.439"))

        # check non-number
        self.assertFalse(main.is_number("b.34"))
