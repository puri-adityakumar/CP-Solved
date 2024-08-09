# https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

class Solution:
    def kthElement(self, k, arr1, arr2):
        arr3 = arr1 + arr2
        arr3.sort()
        for i in arr3:
            return arr3[k - 1]
        