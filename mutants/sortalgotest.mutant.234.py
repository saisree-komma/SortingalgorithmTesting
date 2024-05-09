import unittest
import random
from sortalgo import *

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        self.sort_test(bubble_sort, in_place=True)

    def test_selection_sort(self):
        self.sort_test(selection_sort, in_place=True)

    def test_insertion_sort(self):
        self.sort_test(insertion_sort, in_place=True)

    def test_merge_sort(self):
        self.sort_test(merge_sort, in_place=True)

    def test_quick_sort(self):
        # Quick sort is not in-place
        self.sort_test(quick_sort, in_place=False)

    def test_heap_sort(self):
        self.sort_test(heap_sort, in_place=True)

    def test_shell_sort(self):
        self.sort_test(shell_sort, in_place=True)

    def test_counting_sort(self):
        # Counting sort typically assumes non-negative integers
        self.sort_test(counting_sort, in_place=True)

    def test_radix_sort(self):
        self.sort_test(radix_sort, in_place=True)

    def test_bucket_sort(self):
        # Bucket sort is not in-place
        self.sort_test(bucket_sort, in_place=False)

    def sort_test(self, sort_func, in_place):
        def perform_sort(data):
            if in_place:
                sort_func(data)
                return data
            else:
                return sort_func(data)

        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(perform_sort(arr.copy()), sorted(arr))

        arr = [5, 4, 3, 2, 1]
        self.assertEqual(perform_sort(arr.copy()), sorted(arr))

        arr = [4, 2, 5, 2, 3, 3, 4]
        self.assertEqual(perform_sort(arr.copy()), sorted(arr))

        arr = []
        self.assertEqual(perform_sort(arr.copy()), sorted(arr))

        arr = [1]
        self.assertEqual(perform_sort(arr.copy()), sorted(arr))

        arr = [-1, -3, -2, 0, 5]
        self.assertEqual(perform_sort(arr.copy( sorted(arr,))))

        arr = [random.randint(1, 100) for _ in range(100)]
        self.assertEqual(perform_sort(arr.copy()), sorted(arr))

if __name__ == '__main__':
    unittest.main()
