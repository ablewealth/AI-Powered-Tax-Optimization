import unittest
from utils import calculate_unrealized_gain

class TestUtils(unittest.TestCase):
    def test_calculate_unrealized_gain(self):
        self.assertEqual(calculate_unrealized_gain(100, 150), 50)

if __name__ == '__main__':
    unittest.main()
