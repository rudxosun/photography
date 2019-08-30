N = int(input())
for i in range(N):
    H, W, N = map(int, input().split())

    if N % H == 0:
        X = N//H
    else:
        X = N//H +1
    if N%H == 0:
        Y = H
    else :
        Y = N%H
    print(100*Y + X)

'''
오답노트
꼭대기 층의 경우 일반적인 경우와 다름
'''