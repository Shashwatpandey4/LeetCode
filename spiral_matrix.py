class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top , bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        
        while left<right and top < bottom:
            #spiraling the top row
            for i in range(left, right):
                res.append(matrix[left][i])
            top += 1
            
            #spiraling the right-most column
            for i in range(top,bottom):
                res.append(matrix[i][right -1])
            right -= 1
            
            #If the matrix is just a row or column matrix, end here 
            if not(left<right and top<bottom):
                break
            
            
            #spiraling the bottom row
            for i in range(right -1, left -1,-1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            #spiraling the left-most column
            for i in range(bottom -1, top-1,-1):
                res.append(matrix[i][left])
            left += 1
        
        return res