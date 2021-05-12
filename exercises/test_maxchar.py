import unittest
from maxchar import maxChar


class TestMaxChar(unittest.TestCase):
    def test_maxchar(self):
        inputs = ['', 'a', 'aa', 'abc', 'aab', 'x111', '1221', '!!%&&&&*', '    ', 'abc lilly', 'mam', 'Haha']
        outputs = ['', 'a', 'a', 'a', 'a', '1', '1', '&', '', 'l', 'm', 'a']

        for i in range(len(inputs)):
            with self.subTest(i=i):
                self.assertEqual(maxChar(inputs[i]), outputs[i], "max of {} should be {}".format(inputs[i], outputs[i]))


if __name__ == "__main__":
    unittest.main()
