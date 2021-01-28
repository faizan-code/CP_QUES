n = int(input())
p = list(map(int, input().split()))

for i in range(1,n+1):
    x = (p.index(i)+1)
    z = p.index(x)+1
    print(z)