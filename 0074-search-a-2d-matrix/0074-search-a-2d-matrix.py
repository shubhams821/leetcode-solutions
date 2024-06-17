class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])

        top, bot = 0, Rows-1
        while(top<= bot):
            print(top, bot)
            row = (top + bot)//2

            if matrix[row][0] > target:
                bot = row-1
            elif matrix[row][-1]< target:
                top = row+1
            else:
                break
        row = (top + bot)//2
        l,r = 0, Cols-1

        while(l<=r):
            m = (l+r)//2

            if matrix[row][m] < target:
                l = m+1
            elif matrix[row][m] > target:
                r = m-1
            else:
                return True
        return False