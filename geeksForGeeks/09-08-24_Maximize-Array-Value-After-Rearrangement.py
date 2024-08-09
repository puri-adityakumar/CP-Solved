
# https://www.geeksforgeeks.org/problems/maximize-arrii-of-an-array0026/1

class Solution:
    def Maximize(self, arr):
        if len(arr) == 0:
            return 0

        l = 0
        arr.sort()

        for i in range(len(arr)):
            l = l + (arr[i] * i)
            n = l % (10**9 + 7)
        return n
