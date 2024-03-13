def generate(numRows):
    if numRows <= 2:
        if numRows == 1:
            return [[1]]
        else:
            return [[1],[1,1]]
    else:
        res = [[1],[1,1]] 
        for i in range(2,numRows):
            p1,p2 = 0,1
            length = len(res[i-1])
            res.append([1])
            while p2 < length:
                Sum = res[i-1][p1] + res[i-1][p2]
                res[i].append(Sum)
                p1 += 1
                p2 += 1 
            res[i].append(1)       
        return res              