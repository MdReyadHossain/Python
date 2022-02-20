fib1 = 0
final = 1

n = int(input("Enter the number: "))
print(fib1)
temp = 0
for i in range(1, n+1):
    print(final)
    temp = fib1
    fib1 = final
    final = temp + fib1