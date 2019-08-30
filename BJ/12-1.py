N = int(input())
P1, P2, P3 = 2, 1, 1
if N < 3:
    P1 = 1
else:
    for i in range(N-2):
        P1 = P2 + P3
        P2, P3 = P1, P2
print(P1)