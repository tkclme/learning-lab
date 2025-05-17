# Ecris une fonction qui trie une liste
import unittest

def sort(iteration) -> list:
    iteration_copy = iteration.copy()
    sorted = []
    index = len(iteration) -1

    for i in range(index):
        for j in range(index):
            if iteration[i] < iteration_copy[j]:
                sorted.append[iteration[i]]
                break
            else : greater = iteration[i]
    return sorted.append(greater)

class TestSortFunction(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(first=self.sort([9, 3, 7]), second=[3, 7, 9], msg="Sorted!")
        #self.assertEqual(self.sort([18, 43, 8]), [8, 18, 43])
        #self.assertEqual(self.sort([7, 4, 28, 5, 10, 1]), [1, 4, 5, 7, 10, 28])


if __name__ == '__sort__':
    unittest.sort()
