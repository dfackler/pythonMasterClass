import unittest
import demo

class TestAddMethods(unittest.TestCase):

    def test_negatives(self):
        self.assertEqual(demo.simpleAdd(-1, -2), -3)

    def test_positives(self):
        self.assertEqual(demo.simpleAdd(1,2), 3)

if __name__ == '__main__':
    unittest.main()