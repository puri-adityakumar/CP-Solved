# LINK 🔗 : https://www.geeksforgeeks.org/problems/remove-duplicates3034/1

class Solution:
    def removeDups(self, str):
        seen = set()
        result = []
        for char in str:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)