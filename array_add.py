def divisibleSumPairs(n, k, ar):
    count = 0
    add = list()
    leng = len(ar)
    c = 0
    for i in range(leng-1):

            for l in range(leng-c-1):
                ele = ar[i] + ar[l+1]
                add.append(ele)
                c = c+1



    for n in add:
        if ( n%k == 0 ):
            count = count + 1

    return count


nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
print(divisibleSumPairs(n, k, ar))

