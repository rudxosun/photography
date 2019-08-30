N = int(input())
for i in range(N): #각 거리에 대해서
    X, Y = map(int, input().split())
    D = Y - X
    Even_D = int(2*((D-1)**(0.5)))
    Odd_D = int(2*(D-3/4)**(0.5))
    Result = Odd_D
    print(Even_D, Odd_D, "D = " , D)
    if Even_D != Odd_D:
        Result = Odd_D
    print(Result)





'''
N = int(input())
for i in range(N): #각 거리에 대해서
    X, Y = map(int, input().split())
    D = Y - X
    t = 0
    v = 1
    Distance = 0
    for t in range(1, D+1): # Max of t is D, use break for exit, start at t = 1

        Distance += v
        if Distance == D:
            print(t)
            continue

        if t*(t-1) > D : #감소조건
            v -= 1
        elif t*(t-1) <= D <= (t-1)*(t+1): #유지조건
            pass
        else: #elif (t-1)*(t+1) < D: # 증가조건
            v += 1
        if t == 1 and D <= 3:
            v = 1


        print("v = ", v, "t = ", t, "D = ", D, "Dis = ", Distance)

    print("Rmx")
'''