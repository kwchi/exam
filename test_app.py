import unittest
from app import Pr

class TestPr(unittest.TestCase):
        @unittest.expectedFailure
        def testpr(self):
            expectedresult = 6
            self.assertEqual(self.pr.progression(1, 1, 3), expectedresult)

if __name__ == "__main__":
    unittest.main()