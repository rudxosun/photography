N = int(input()) # N < 1000
#자리수에 따라 결정
NumOfHan = 0
if N < 100:
    NumOfHan = N
elif  N > 99: # 3자리수면
    for i in range(100, N+1): #100~999
        if i == 1000:
            continue
        if int(str(i)[0]) + int(str(i)[2]) == 2*int(str(i)[1]):
            NumOfHan += 1
    NumOfHan += 99
print(NumOfHan)


