def arrangeCoins(n):
        total = 0
        row = 0
        while total <= n:
           row += 1
           total += row
        #check the breaking condition and return the row if the total is greater than n means we have to return the previous row
        return row - 1 if total > n else row   
print(arrangeCoins(800)) 