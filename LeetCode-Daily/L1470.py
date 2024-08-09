# https://leetcode.com/problems/shuffle-the-array/description/?source=submission-ac


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for a, b in zip(nums[:n], nums[n:]):
            result.append(a)
            result.append(b)
        return result
