N = int(input())
for i in range(N):
    M, N, x, y = map(int, input().split())
    if x == M:
        x == 0
    if y == N:
        y == 0
    answer = " "
    for m in range(M):
        for n in range(N):
            if M*m + x == N*n + y :
                if answer == " ":
                    answer = N*n + y
    if answer == " " :
        answer = -1

    print(answer)

'''
다시풀자
노가다 말고 다른 방법을 찾자

'''