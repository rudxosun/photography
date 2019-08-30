A, B, C = map(int, input().split())

if C > B :
    n = A//(C-B)
    N = n + 1
    print(N)
else :
    print(-1)

'''
N = 0
while True:
    N += 1
    if (N-1) < (A+B*N)/C and  (A+B*N)/C < N:
        print(N)
        break
'''
"""
이런 노가다 말고도 방법이 있을텐데

1000 70 170

오답노트
문제를 제대로 안읽음 + 올림을 math로 안하고 //를 사용 후 +1해도 가능
"""