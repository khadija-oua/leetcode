class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0]) - 1
        z=-1
        for i in range(n):
            if target <= matrix[i][m] and target >=matrix[i][0]:
                z=i
        if z == -1 : return False
        low = 0
        high = m 
        while low <= high : 
            mid = (low + high)//2 
            if matrix[z][mid] == target :
                return True 
            elif matrix[z][mid] < target:
                low = mid + 1
            else : 
                high = mid - 1 
        return False
        
            