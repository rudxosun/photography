import math
N = int(input())
for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    Dis_Point = math.sqrt((x2-x1)**2+(y2-y1)**2)
    Sum_r = r1 + r2
    Dif_r = abs(r1 - r2)
    if (x1, y1, r1) == (x2, y2, r2) :
        print(-1)
        continue
    elif Dif_r < Dis_Point:
        if Dis_Point > Sum_r:
            print(0)
        elif Dis_Point == Sum_r :
            print(1)
        elif Dis_Point < Sum_r :
            print(2)
    elif Dif_r >= Dis_Point:
        if Dif_r == Dis_Point:
            print(1)
        elif Dif_r > Dis_Point:
            print(0)
    else:
        print("이럴리 없는데...")

