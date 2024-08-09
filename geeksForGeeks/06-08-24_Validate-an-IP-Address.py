# https://www.geeksforgeeks.org/problems/validate-an-ip-address-1587115621/1

class Solution:
    def isValid(self, s):
        l = len(s)
        if l > 15:
            return False
        temp = list(map(str, s.split('.')))
        if len(temp) != 4:
            return False
        for i in temp:
            if not i or not (0 <= int(i) <= 255):
                return False
            if len(i) > 1 and i[0] == '0':
                return False
        return True