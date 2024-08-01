## Link🔗 : https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

class Solution:
    def spirallyTraverse(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            
            if not matrix:
                break

            # Transpose the matrix
            #  matrix = list(zip(*matrix))[::-1] # The entire transpose the matrix block can be solved by one single line
            transposed_matrix = []
            for i in range(len(matrix[0])):
                new_row = []
                for row in matrix:
                    new_row.append(row[i])
                transposed_matrix.append(new_row)

            # Reverse the rows
            matrix = transposed_matrix[::-1]

        return result