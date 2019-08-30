import math
N = int(input())
M = math.log(N,3)
P = ''
for i in range(N):
    for j in range(N):
        if j/3 < 3 :
            if j == 2:
                P += ''
            P += '*'
        else :
            P += ''

    print(P)
    P = ''






'''
1 3 7 9 19 21 25 27

n x n

***
* *
   
   
'''