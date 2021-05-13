import unittest
from anagrams import anagrams


class TestAnagrams(unittest.TestCase):
    def test_anagrams(self):
        true_inputs = [
            ('', ''),
            ('a', 'a'),
            ('aa', 'aa'),
            ('ab', 'ab'),
            ('post', 'stop'),
            ('hi there', 'there hi'),
            ('Hello', 'olleh'),
            ("It's a beautiful day!", "its beautiful Daya"),
            ('12345', '15243'),
            ('9 to 5', 'O-95-t'),
            ('&#!@', ''),
            ('TOTAL', 'lotta')
        ]

        false_inputs = [
            ('', '1'),
            ('abc', 'xyz'),
            ('aabbcc', 'abc'),
            ('aaa', 'aab'),
            ('Hi there!', 'Hello there!')
        ]

        for i in true_inputs:
            with self.subTest(i=i):
                self.assertTrue(anagrams(i[0], i[1]), "{} and {} are anagrams".format(i[0], i[1]))

        for i in false_inputs:
            with self.subTest(i=i):
                self.assertFalse(anagrams(i[0], i[1]), "{} and {} are not anagrams".format(i[0], i[1]))


if __name__ == "__main__":
    unittest.main()
