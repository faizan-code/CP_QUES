for i in range(int(input())):
    x,y,z = map(int, input().split())
    if abs(z-x) == abs(z-y):
        print('Mouse C')
    elif abs(z-x) < abs(z-y):
        print('Cat A')
    else:
        print('Cat B')