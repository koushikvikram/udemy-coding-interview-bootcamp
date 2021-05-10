import unittest
from reversestring import reverse


class TestStringReverse(unittest.TestCase):
    def test_reverse(self):
        inputs = ['abcd', '  abcd', 'a', '', 'Greetings!', 'a\nb', '\t\n', 'Thank you!']
        outputs = ['dcba', 'dcba  ', 'a', '', '!sgniteerG', 'b\na', '\n\t', '!uoy knahT']
        
        for i in range(len(inputs)):
            with self.subTest(i=i):
                self.assertEqual(
                    reverse(inputs[i]), 
                    outputs[i], 
                    'Reverse of {} should be {}'.format(inputs[i], outputs[i])
                    )


if __name__ == "__main__":
    unittest.main()
