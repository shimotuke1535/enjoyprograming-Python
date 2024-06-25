i = 1
A = int(input("Input A:"))
while A >= 1:
    print(A)
    i = i + 1
    if A % 2 == 0:
        A = int(A / 2)
    else:
        A = int(3 * A + 1)
    
    if A == 1:
        break
print("Count:",i)