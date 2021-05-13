import unittest
from chunk import chunk


class TestChunk(unittest.TestCase):
    def test_chunk(self):
        in_arr_0 = []
        in_arr_1 = [1]
        in_arr_2 = [1, 2, 3]
        in_arr_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        in_arr_4 = [1, 1, 1, 1, 1]

        out_arr_0 = []
        out_arr_1 = [
            [1]
            ]
        out_arr_2 = [
            [1], 
            [2], 
            [3]
            ]
        out_arr_3 = [
            [1, 2, 3, 4, 5], 
            [6, 7, 8, 9, 10], 
            [11, 12]
            ]
        out_arr_4 = [
            [1, 1, 1], 
            [1, 1]
            ]

        inputs = [
            (in_arr_0, 2), 
            (in_arr_1, 3), 
            (in_arr_2, 1), 
            (in_arr_3, 5),
            (in_arr_4, 3)
            ]

        outputs = [
            out_arr_0,
            out_arr_1,
            out_arr_2,
            out_arr_3,
            out_arr_4
            ]
        
        for i in range(len(inputs)):
            with self.subTest(i=i):
                self.assertEqual(
                    chunk(inputs[i][0], inputs[i][1]), 
                    outputs[i], 
                    "chunk({}, {}) should be {}".format(
                        inputs[i][0], 
                        inputs[i][1], 
                        outputs[i]
                        )
                    )


if __name__ == "__main__":
    unittest.main()
