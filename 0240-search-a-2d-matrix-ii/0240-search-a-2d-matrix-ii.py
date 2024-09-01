class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while target > matrix[i][i]:
            if i+1 == len(matrix) or i+1 == len(matrix[0]):
                break
            i+=1
        i,j = i,i
        while i< len(matrix):
            l,r =0, len(matrix[0])
            while l<=r:
                m = (l+r)//2
                if m >= len(matrix[0]):
                    break
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] > target:
                    r = m-1
                elif matrix[i][m] < target:
                    l = m+1
            i+=1
        while j< len(matrix[0]):
            l, r =0, len(matrix)
            while l<=r:
                m = (l+r)//2
                if m >= len(matrix):
                    break
                if matrix[m][j] == target:
                    return True
                elif matrix[m][j] > target:
                    r = m-1
                elif matrix[m][j] < target:
                    l = m+1
            j+=1
        return False