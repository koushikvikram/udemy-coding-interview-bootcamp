import unittest
from capitalize import capitalize

class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        inputs = ['', 'a', 'ab', 'hi there', 'how are you?', ' there is a leading space', 'there is a trailing space ', ' there are spaces on both sides ']
        outputs = ['', 'A', 'Ab', 'Hi There', 'How Are You?', ' There Is A Leading Space', 'There Is A Trailing Space ', ' There Are Spaces On Both Sides ']
        for i in range(len(inputs)):
            with self.subTest(i=i):
                self.assertEqual(
                    capitalize(inputs[i]), 
                    outputs[i], 
                    "Capitalized version of '{}' should be '{}'".format(
                        inputs[i],
                        outputs[i]
                    )
                )


if __name__ == "__main__":
    unittest.main()
    