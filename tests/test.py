
import unittest
from drone_test import hello, hi

class SomeTest(unittest.TestCase):
    """
    Test packages utilities functions
    """
    print("hey-ya")
    print("hey-you")
    def test_test(self):
        self.assertEqual(hello(), "hello world")
        self.assertEqual(hi(), "hi")

if __name__ == "__main__":
    unittest.main()