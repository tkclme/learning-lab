import unittest
from sort import mySortFunction as sort


class TestSortFunction(unittest.TestCase):
    def testSortingList(self):
        a = [11, 5, 7, 3, 2, 15]
        b = sort(a)
        print(b)
        self.assertEqual(b, [2, 3, 5, 7, 11, 15])

if __name__ == "__main__":
    unittest.main()