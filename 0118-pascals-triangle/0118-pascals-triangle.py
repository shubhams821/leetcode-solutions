class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res  = [[1]]

        for i in range(numRows-1):
            temp = [0]+ res[-1]+[0]
            tmp = []
            for j in range(len(temp)-1):
                tmp.append(temp[j]+ temp[j+1])
            res.append(tmp)
        return res
