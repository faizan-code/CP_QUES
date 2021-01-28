n,k,q = map(int, input().split())
arr = list(map(int, input().split()))
arr = (arr[len(arr) - k:len(arr)]
              + arr[0:len(arr) - k])
for i in range(q):
    a = int(input())
    print(arr[a])