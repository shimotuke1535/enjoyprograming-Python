import random
flag = 0
list = []
D = int(input("How many lists in number:"))
for i in range(0,D,1):
    list.append(int(random.uniform(-1000,1000)))
for i in range(D):
    print(list[i])
i = 0
I = 0
k = 0
temp = 0
mode = input("Up or Down:")
while flag == 0:
    if mode == "Down":
        if list[i] < list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
        else:
            k = k + 1
    if mode == "Up":
        if list[i] > list[i+1]:
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp
        else:
            k = k + 1
    i=i+1
    if i >= D-1:
        i = 0
        k = 0
        I = 1 + I
    if k >= D-2:
        print("Count:",I)
        break
for i in range(D):
    print(list[i])