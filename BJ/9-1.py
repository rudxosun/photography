N = int(input())
N_list = list(map(int, input().split()))
count = 0
for i in range(N):
    Switch = True
    for j in range(2,1000): #1을 안넣는 이유 : 소수(1과 자기자신을 제외한 수로 나눠지지 않는 수)
        if N_list[i] % j == 0 and N_list[i] != j: #자기자신을 제외한 숫자로 나눠지면
            Switch = False #False가 됨
    if Switch and N_list[i] !=1: #하지만 1은 소수로 안쳐줌
        count += 1
print(count)

'''
for i in range(2,1000): # 천개 중에서 리스트에 있는 숫자를 나누고, 나눠지면 리스트에서 제거
    for j in range(len(N_list)):
        if N_list[j] % i == 0 :

print(len(N_list))

'''