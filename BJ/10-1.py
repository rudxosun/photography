N, M = map(int, input().split())
Cards = list(map(int, input().split()))
result = 0
Diff = 300000
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k and k != i:
                Sum = (Cards[i] + Cards[j] + Cards[k])
                if abs(Sum - M) < Diff and Sum <= M:
                    result = Sum
                    Diff = abs(Sum - M)

print(result)

'''
오답노트
result설정할 때 Diff를 설정 안함
'''
