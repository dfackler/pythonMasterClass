import unittest
import demo

class TestAddMethods(unittest.TestCase):

    def test_negatives(self):
        self.assertEqual(demo.simpleAdd(-1, -2), -3)

    def test_positives(self):
        self.assertEqual(demo.simpleAdd(1,2), 3)

    def test_norm_div(self):
        self.assertAlmostEqual(demo.simpleDiv(1,2), .5)

    def test_zero_div(self):
        self.assertEqual(demo.simpleDiv(1,0), None)
    
    def test_string_div(self):
        self.assertEqual(demo.simpleDiv("hello", 2), None)

    def test_string_count(self):
        self.assertEqual(demo.sumDigits("12345"), 5)
    
    def test_int_count(self):
        self.assertEqual(demo.sumDigits(12345), None)

if __name__ == '__main__':
    unittest.main()