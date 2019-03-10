
import unittest
from drone_test import hello

class SomeTest(unittest.TestCase):
    """
    Test packages utilities functions
    """
    def test_test(self):
        self.assertEqual(hello(), "hello world")

if __name__ == "__main__":
    unittest.main()