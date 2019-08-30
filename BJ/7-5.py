S = input()
S_Num = []
L_Num = []
Num = []
Answer = 0

for i in range(65, 91):
    S_Num.append(S.count(chr(i)))
    L_Num.append(S.count(chr(i+32)))

for j in range(26):
    Num.append(S_Num[j] + L_Num[j])


for i in range(26):
    if Num[i] == max(Num):
        if Answer == 0:
            Answer = chr(i+65)
        else:
            Answer = "?"

print(Answer)

"""
오답노트
list + list = list의 연장.
요소끼리의 합은 append등을 사용해서 나타냄.
"""
