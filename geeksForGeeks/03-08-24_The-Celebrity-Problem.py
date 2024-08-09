# https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

class Solution:
    
    def celebrity(self, mat):
        array_size = len(mat)
        
        a = 0
        b = array_size - 1
        
        while a < b:
            if mat[a][b] == 1:
                a += 1
            else:
                b -= 1
        
        for i in range(array_size):
            if i != a and (mat[a][i] == 1 or mat[i][a] == 0):
                return -1
        
        return a

