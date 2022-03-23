def dectobin(n):
    if n >= 1:
        dectobin(n // 2)
    print(n % 2, end = '')

n = 6
fitness = []
sum = 0

for i in range(0, n):
    x = int(input("Enter number: "))
    print("number : " , dectobin(x))
    fun = (15 * x) - (x*x)
    fitness.append(fun)
    sum = fun + sum

print("\nDecode fitness = " , fitness)
print("\nSum of Decode fitness = " , sum)