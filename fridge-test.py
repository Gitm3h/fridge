import unittest
from fridge import evaluate


class FridgeTests(unittest.TestCase):
    contents = ["A","B","C"]

    def test_evaluate_both_found(self):
      first = "B"
      result = evaluate(self.contents, first, "C")
      self.assertEqual(result, 2)

    def test_evaluate_both_both_but_are_lowercase(self):
      result = evaluate(self.contents, "a", "b")
      self.assertEqual(result, 2)

    def test_evaluate_neither_found(self):
      result = evaluate(self.contents, "???", "?!")
      self.assertEqual(result, 0)

    def test_evaluate_found_notfound(self):
      result = evaluate(self.contents, "A", "X")
      self.assertEqual(result, 1)

    def test_evaluate_notfound_found(self):
      result = evaluate(self.contents, "X", "B")
      self.assertEqual(result, 1)
    
    def test_evaluate_both_found_but_both_same(self):
      result = evaluate(self.contents, "a", "a")
      self.assertEqual(result, 1)




if __name__ == '__main__':
    unittest.main()


