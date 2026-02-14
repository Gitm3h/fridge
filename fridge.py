import unittest
from fridge import evaluate

# This fails, WTF?

class FridgeTests(unittest.TestCase):
    def test_evaluate(self):
        result = evaluate(["a","b"], ["a", "b"])
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
