n,m=input().strip().split()
n=int(n)
m=int(m)
p=[1 for i in range(m-n+1)]
for i in range(2,100000):
    k=((n-1)//i+1)*i
    if k==i:
        k+=i
    while k<=m:
        p[k-n]=0
        k+=i
ans=0
for i in range(m-n-1):
    if p[i]+p[i+2]==2:
        ans+=1
if n==1 and ans>0:
    ans-=1
print(ans)