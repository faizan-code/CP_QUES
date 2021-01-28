sum = 0
people = 5
for i in range(int(input())):
    receive = int(people//2)
    sum = sum+receive
    people = (people - receive)*3

print(sum)
