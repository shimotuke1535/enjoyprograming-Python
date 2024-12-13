i = 1
flag = 0
A = int(input("Input A:"))
while A >= 1:
    print(A)
    if flag == 1:
        break
    if A % 2 == 0:
        i = i + 1
        A = int(A / 2)
    else:
        i = i + 1
        A = int(3 * A + 1)
    if A == 1:
        flag = flag + 1
print("Count:",i)