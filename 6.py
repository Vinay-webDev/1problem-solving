"""54. Spiral Matrix"""
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
class Solution:
    def spiralMatrix(self, matrix):
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                res.append(matrix[i][j])
        return res
sol = Solution()
print(sol.spiralMatrix(matrix1))