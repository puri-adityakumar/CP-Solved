# https://www.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):

        arr3 = arr1 + arr2
        arr3.sort()

        mid_index = len(arr3) // 2

        if len(arr3) % 2 == 0:
           return arr3[mid_index - 1] + arr3[mid_index]
        else:
            return arr3[mid_index]




