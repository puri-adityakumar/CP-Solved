## https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
        
        def is_valid(x, y):
            return 0 <= x < len(m) and 0 <= y < len(m[0]) and m[x][y] == 1
        
        def backtrack(x, y, path):
            if x == len(m) - 1 and y == len(m[0]) - 1:
                result.append(path)
                return
            for dx, dy, direction in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    m[nx][ny] = 0  
                    backtrack(nx, ny, path + direction)
                    m[nx][ny] = 1  
        
        result = []
        if m[0][0] == 1:  
            m[0][0] = 0  
            backtrack(0, 0, '')
            m[0][0] = 1  
        return sorted(result)