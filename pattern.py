class pattern:
    def __init__(obj, row):
        obj.row = row

    def pat_num(obj):
        for i in range(1, obj.row + 1):
            for j in range(1, i + 1):
                print(j , end = " ")
            print(" ")
    
    def pat_star(obj):
        n = obj.row - 1
        for i in range(0, obj.row):
            for j in range(0,n):
                print(end=" ")
            n = n - 1
            for j in range(0, i+1):
                print("*", end=" ")
            print("\r")

    def pat_rev_star(obj):
        n = 2 * obj.row - 2
        for i in range(0, obj.row):
            for j in range(0, n):
                print(end=" ")
            n = n - 2
            for j in range(0, i + 1):
                print("* ", end="")
            print("\r")



n = int(input("Enter row : "))
p = pattern(n)
print("Number Pyramid: ")
p.pat_num()
print("\nStar Pyramid: ")
p.pat_star()
print("\nStar Reverse Pyramid: ")
p.pat_rev_star()