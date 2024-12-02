import unittest
from app import Pr

class TestPr(unittest.TestCase):
        
        def setUp(self):
            self.pr = Pr()

        @unittest.expectedFailure
        def testpr(self):
            expectedresult = 7
            self.assertEqual(self.pr.progression(1, 1, 3), expectedresult)

if __name__ == "__main__":
    unittest.main()