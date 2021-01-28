#!/bin/python3
def bonAppetit(bill, k, b):

    total = sum(bill)
    a_bill = (total-bill[k])/2
    if (a_bill == b):
        print("Bon Appetit")
    else:
        print(int(b-a_bill))

nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bonAppetit(bill, k, b)
