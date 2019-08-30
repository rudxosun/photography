N = int(input())
N_list = []
for i in range(N):
    N_list.append(int(input()))
N_list.sort()
for i in range(N):
    print(N_list[i])
