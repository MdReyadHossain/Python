n = int(input("Input the number of terms = "))
sum = 0

for i in range(1, n+1):
    print("1/{}".format(i), end="")
    if i == n:
        print(" = ", end = "")
    else:
        print(" + ", end = "")

    sum = sum + 1.0/i

print(round(sum, 6))