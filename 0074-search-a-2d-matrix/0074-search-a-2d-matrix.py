class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row, Cols = len(matrix), len(matrix[0])

        top = 0
        bot = Row-1
        while(top <= bot):
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top= row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
        if (top>bot):
            return False
        row = (top+bot)//2
        l=0
        r=Cols-1
        while(l<=r):
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target <matrix[row][m]:
                r = m-1
            else:
                return True
        m = (l+r)//2
        return False
