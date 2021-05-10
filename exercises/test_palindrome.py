import unittest
from palindrome import palindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        palindromes = ['aa', 'mam', '1001', 'Fish hsiF', '!oxo!', ' tat ']
        not_palindromes = [' abc', 'def ', 'hello', 'Madam', 'modem']

        for p in palindromes:
            with self.subTest(i=p):
                self.assertTrue(palindrome(p), "{} is a palindrome".format(p))

        for np in not_palindromes:
            with self.subTest(i=np):
                self.assertFalse(palindrome(np), "{} is not a palindrome".format(np))

        
if __name__ == "__main__":
    unittest.main()
