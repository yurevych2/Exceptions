import unittest
import vigenere_cipher

class TestVigenereCipher(unittest.TestCase):
    
    def test_extend_keyword(self):
        cipher = vigenere_cipher.VigenereCipher()
        cipher.init('word')
        self.assertEqual(cipher.extend_keyword(7), 'wordwor')
        self.assertEqual(cipher.extend_keyword(9), 'wordwordw')
        self.assertEqual(cipher.extend_keyword(11), 'wordwordwor')
    
    def test_combine_character(self):
        self.assertEqual(vigenere_cipher.combine_character('A', 'C'), 'C')
        self.assertEqual(vigenere_cipher.combine_character('Z', 'H'), 'G')
        self.assertEqual(vigenere_cipher.combine_character('B', 'X'), 'Y')
        self.assertEqual(vigenere_cipher.combine_character(' ', 'G'), 'Z')
    
    def test_separate_character(self):
        self.assertEqual(vigenere_cipher.separate_character('G', 'H'), 'Z')
        self.assertEqual(vigenere_cipher.separate_character('Z', 'Z'), 'A')
        self.assertEqual(vigenere_cipher.separate_character('B', 'A'), 'B')
        self.assertEqual(vigenere_cipher.separate_character(' ', 'G'), 'N')
    
    def test_encode(self):
        cipher = vigenere_cipher.VigenereCipher()
        cipher.init('FUCK')
        self.assertEqual(cipher.encode('i love anime'), 'NFQFJUPSRY')
    
    def test_decode(self):
        cipher = vigenere_cipher.VigenereCipher()
        cipher.init('FUCK')
        self.assertEqual(cipher.decode('NFQFJUPSRY'), 'ILOVEANIME')

if __name__ == '__main__':
    unittest.main()
