## Link 🔗 : https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1

class Solution:
    def longestCommonPrefix(self, strings):
        if not strings:
            return "-1"

        strings.sort()
        shortest = strings[0]
        longest = strings[-1]
        prefix_length = 0

        while prefix_length < len(shortest) and prefix_length < len(longest) and shortest[prefix_length] == longest[prefix_length]:
            prefix_length += 1

        if prefix_length == 0:
            return "-1"

        return shortest[:prefix_length]