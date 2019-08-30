




"""
너무 수학적인 접근.
from math import factorial
N = int(input())
count = 0
for i in range(N+1):
    if (N - i)%2 == 0:
        j = (N - i)//2
        if i != 0 and j != 0:
            count += (factorial((i+j))/(factorial(i)))*(factorial(j))
            print(i, j)
        else:
            count += 1
            print("else")

print(count)
"""