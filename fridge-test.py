import unittest
from fridge import evaluate

# This fails, WTF?

class FridgeTests(unittest.TestCase):
    def test_evaluate(self):
        result = evaluate(["a","b"], ["a", "b"])
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
