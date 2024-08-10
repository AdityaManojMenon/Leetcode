class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols = len(matrix),len(matrix[0])
        self.sumMatrix = [[0] * (cols+1) for r in range(rows+1)]
        
        for r in range(rows):
            prefix_sum = 0
            for c in range(cols):
                prefix_sum += matrix[r][c]
                above = self.sumMatrix[r][c+1] #the row above the last row for which we are calculating
                self.sumMatrix[r+1][c+1] = prefix_sum + above
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 # offset all the values by one
        bottom_corner = self.sumMatrix[row2][col2]
        above = self.sumMatrix[row1-1][col2]
        left = self.sumMatrix[row2][col1-1]
        top_corner = self.sumMatrix[row1-1][col1-1]
        
        return bottom_corner - above - left + top_corner
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)