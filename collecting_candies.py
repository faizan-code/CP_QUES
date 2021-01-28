# Problem Description
#
# Question:- Krishna loves candies a lot, so whenever he gets them,
# he stores them so that he can eat them later whenever he wants to.
#
# He has recently received N boxes of candies each containing
# Ci candies where Ci represents the total number of candies
# in the ith box. Krishna wants to store them in a single box.
# The only constraint is that he can choose any two boxes and
# store their joint contents in an empty box only. Assume that
# there are an infinite number of empty boxes available.
#
# At a time he can pick up any two boxes for transferring
# and if both the boxes contain X and Y number of candies
# respectively, then it takes him exactly X+Y seconds of
# time. As he is too eager to collect all of them he has
# approached you to tell him the minimum time in which all
# the candies can be collected.

# Input Format:
#
# The first line of input is the number of test case T
# Each test case is comprised of two inputs
# The first input of a test case is the number of boxes N
# The second input is N integers delimited by whitespace denoting the number of candies in each box
# Output Format: Print minimum time required, in seconds, for each of the test cases. Print each output on a new line.
#
# Constraints:
#
# 1 < T < 10
# 1 < N< 10000
# 1 < [Candies in each box] < 100009

t = int(input())
time = list()
sum1 = 0
t_time = list()

for i in range(t):
    n_box = int(input())
    candies = list(map(int, input().rstrip().split()))
    candies.sort(reverse=False)
    while (len(candies) >= 2):
       candies.sort(reverse=False)
       sum1 = candies[0] + candies[1]
       candies.pop(0)
       candies.pop(0)

       # NOTE pop mee index value use krte hai

       candies.append(sum1)
       time.append(sum1)

    # here after while loop is finished then we need to add
    # sum elements in the list

    s = sum(time)
    t_time.append(s)


for times in t_time:
    print(times,end=" ")





