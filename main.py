class NumPyramid:
    def __init__(self,n):
        self.n=n

    def printNumPyramid(self):
        m=self.n
        for x in range (self.n):
            for y in range(m):
                print(end=' ')
                m -= 1
            for y in range (x+1):
                print("*",end=' ')
            print()

k = NumPyramid(int(5))
k.PrintNumPyramid()