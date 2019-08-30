M, N = map(int, input().split())
N_list = [True]*(N+1)
for i in range(2, int(N**0.5) + 1): #2부터 하나씩 나누면서 갈거임
    if N_list[i] == True:
        for j in range(i*2, N+1, i):
            N_list[j] = False
for i in range(N+1):
    if N_list[i] == True and i >= M and i != 1:
        print(i)


"""
오답노트
에라토스테네스의 채 구현하기 힘들어유,,,
+ N_list 의 인덱스 자체를 활용했기 때문에 N_list[0]은 없는 취급
  => 곧 숫자의 개수를 N+1개로 활용해야했음
"""

'''
슈ㅏ 뭐가 틀렸을까
M, N = map(int, input().split())
N_list = [True]*(N+1)
for i in range(2, int(N**0.5)+1):
    if N_list[i] == True:
        for j in range(2*i,N,i):
            N_list[j] = False
for i in range(N):
    if N_list[i] == True and i >= M:
        print(i)

'''




'''
시간초과
#M 부터 N까지 범위의 i
for i in range(M, N):
    Switch = True

    for j in range(2,N):
        if i % j == 0 and i != j : #자기자신을 제외한 숫자로 나눠지면
            Switch = False
            break

    if Switch == True and i != 1: # 1은 소수가 아님
        print(i)



#i 가 M부터 N까지의 j에게 나눠지지 않는다면 list에 추가 (단 i가 1일 경우 추가안함)
# 한 줄씩 띄워서 리스트 요소 출력

'''