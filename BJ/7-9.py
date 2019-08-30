S = list(input())
count = 0
for i in range(len(S)):
    count += 1
    if S[i] == "=":
        if S[i-1] == "c" or S[i-1] == "s":
            count -= 1
    if S[i] == "-":
        if S[i-1] == "c" or S[i-1] == "d":
            count -= 1
    if S[i] == "=":
        if S[i-1] == "z":
            if S[i-2] == "d":
                count -=2
            else :
                count -=1
    if S[i] == "j":
        if S[i-1] == "l" or S[i-1] == "n":
            count -= 1


print(count)

# good!



