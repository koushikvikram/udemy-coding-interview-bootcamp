import unittest
from reverseint import reverseInt


class TestReverseInt(unittest.TestCase):
    def test_reverse_int(self):
        inputs = [0, 1, 10, 100, 11, 12, 987654, 77777, -1, -11, -12, -10, -12345, -999]
        outputs = [0, 1, 1, 1, 11, 21, 456789, 77777, -1, -11, -21, -1, -54321, -999]
        for i in range(len(inputs)):
            with self.subTest(i=i):
                self.assertEqual(reverseInt(inputs[i]), outputs[i], 'Reverse of {} is {}'.format(inputs[i], outputs[i]))


if __name__ == "__main__":
    unittest.main()
