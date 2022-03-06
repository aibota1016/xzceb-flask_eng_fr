import unittest
import translator

class Tests(unittest.TestCase):

    def testEnglishToFrench(self):
        test1 = translator.english_to_french('Hello')['translations'][0]['translation']
        self.assertEqual(test1, 'Bonjour')

    def testFrenchToEnglish(self):
        test1 = translator.french_to_english('Bonjour')['translations'][0]['translation']
        self.assertEqual(test1, 'Hello')

if __name__ == '__main__':
    unittest.main()
