a, b = map(int, input().split(" "))
a_r = int(str(a)[::-1])
b_r = int(str(b)[::-1])
print(max(a_r, b_r))












"""
노트
리스트나 문자열을 역순으로 보낼 떄
N[::-1]
"""