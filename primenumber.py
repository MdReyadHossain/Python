import math

cnt = 0
n = int(input("Enter a number: "))

if n > 2:
    for i in range(2, int(math.sqrt(n)), 1):
        if n%i == 0:
            print("Non-Prime!")
            cnt += 1
            break

    if cnt == 0:
        print("Prime Number!")
    
elif n < 0:
    print("Negative not valid!!")

else:
    print("Non-Prime!")