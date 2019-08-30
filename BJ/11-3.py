import sys
N = int(sys.stdin.readline())
M = 10000
P = [0]*(M+1)
for i in range(N):
    P[int(sys.stdin.readline())] += 1
for i in range(M+1):
    print("%s\n"%i*P[i], end="")
"""
오답노트
시간초과 : sys.stdin.readline()을 활용
메모리 초과 : 모두 0인 리스트는 그렇게 크지 않음. 이렇게 범위를 지정해 주는 것이 더 효과적
인덱스 붙이기 : 그냥 모두 0인 리스트 활용하여 list의 인덱스를 활용
"""


'''
import sys
N = int(input())
N_list = []
#만들어야 할 것 [[1, 1의개수], [2, 2의개수]...]
for i in range(N): #주어진 숫자
    Num = int(sys.stdin.readline())
    Switch = True
    for j in range(len(N_list)):
        if N_list[j][0] == Num:
            N_list[j][1] += 1
            Switch = False
    if Switch == True:
        N_list.append([Num, 1])

S_N_list = sorted(N_list, key= lambda Num : Num[0])

for i in range(len(S_N_list)):
    for j in range(S_N_list[i][1]):
        print(S_N_list[i][0])


-----------------------------------------------------
        
    N_list.append(int(input()))
N_list.sort()
for i in range(N):
    print(N_list[i])
    '''
