def queenAttack(n,k,qr,qc,obstacles):
    left = qc - 1
    right = n - qc
    top = n - qr
    bottom = qr - 1
    tl = left if top >= left else top
    tr = right if top >= right else top
    dl = left if left <= bottom else bottom
    dr = right if right <=bottom  else bottom

    # now if obstacles is present

    for obst in obstacles:
        row = obst[0]
        col = obst[1]

        if row==qr and col < qc:

            left = qc-col-1
        if col > qc and row == qr:
            right = col - qc - 1
        if col == qr and row > qr:
            top = row - qr - 1
        if col == qc and row < qr:
            bottom = qr - row - 1
        if col < qc and row > qr:
            if row - qr == qc - col:
                tl = qc - col - 1
        if col > qc and row > qr:
            if row - qr == col - qc:
                tr = col - qc - 1
        if col < qc and row < qr:
            if qc - col == qr - row:
                dl = qc - col - 1
        if row < qr and col > qc:
            if qr - row == col - qc:
                dr = col - qc - 1


    return left+right+top+bottom+dl+dr+tl+tr

n,k = map(int, input().split())
qr,qc = map(int, input().split())
obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))


result = queenAttack(n,k,qr,qc,obstacles)
print(result)