'''
N = input()
N_list = list(map(int, input().split()))
print(max(N_list), min(N_list))
'''
N = int(input())
K = int( (3+((9+12*(N-2))**0.5))/6 )
print(K+1)