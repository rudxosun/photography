N = int(input())
N_list = []
for i in range(N):
    x, y = map(int, input().split())
    N_list.append((x+100000) + 1000000*(y+100000))
N_list.sort()
for i in range(N):
    print(N_list[i]%1000000 -100000, N_list[i]//1000000 - 100000)
