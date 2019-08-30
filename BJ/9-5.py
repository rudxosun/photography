

M = 10000
D_list = []

M_list = [True]*(M+1)
for i in range(2, int(M**0.5) + 1): #2부터 하나씩 나누면서 갈거임
    if M_list[i] == True:
        for j in range(i*2, M+1, i):
            M_list[j] = False

for i in range(M+1):
    if M_list[i] == True and i != 1:
        D_list.append(i)

L = int(input())

for i in range(L):
    N = int(input())
    n = int(N/2)
    for a in range(n, len(M_list)):#소수의 리스트[n-1:]: #[t,t,t,f,f,t,f,t,]
        if M_list[a] == True and (N - a) in D_list:
            print(N - a, a)
            break

