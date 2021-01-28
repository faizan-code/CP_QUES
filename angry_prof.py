def punishment(a,k):
    count = 0
    for i in a:
        if i <= 0:
            count = count+1
    if count >= k:
        print('NO')
    else:
        print('YES')
for i in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    punishment(a,k)