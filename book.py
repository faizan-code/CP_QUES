n = int(input())
p = int(input())
y = 0
if p > n//2:
    x = n-p

    if x == 1 and n%2 == 0:
        y = 1
        print(y)
    elif x == 1 and n%2 != 0:
        y = 0
        print(y)
    else:

        print(x//2)
else:
    print(p//2)