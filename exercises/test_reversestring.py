import unittest
from reversestring import reverse

class TestStringReverse(unittest.TestCase):
    def test_reverse(self):
        test_inputs = ['abcd', '  abcd', 'a', '', 'Greetings!', 'a\nb', '\t\n', 'Thank you!']
        expected_outputs = ['dcba', 'dcba  ', 'a', '', '!sgniteerG', 'b\na', '\n\t', '!uoy knahT']
        for i in range(len(test_inputs)):
            self.assertEqual(
                reverse(test_inputs[i]), 
                expected_outputs[i], 
                'Reverse of {} should be {}'.format(test_inputs[i], expected_outputs[i])
                )

if __name__ == "__main__":
    unittest.main()