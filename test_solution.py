import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_question(self):
        self.assertEqual(self.solution.solve_first_question(), 14, "Should be 14 pokemon with 'at' in their name and with 2 'a' in their name, including the first 'at'")

    def test_second_question(self):
        self.assertEqual(self.solution.solve_second_question(), 294, "Should be 294 pokemon species that can procreate Raichu")

    def test_third_question(self):
        self.assertEqual(self.solution.solve_third_question(), [1300, 195], "Answer should be [1300, 195]")

if __name__ == '__main__':
    unittest.main()