import random
import time
import datetime
import os
flag = 0
z = 0
list = []
now = datetime.datetime.now()
os.chdir(os.path.dirname(__file__))
Data_name = os.path.dirname(__file__) + "/Data/" + "sort_" + now.strftime("%Y%m%d_%H%M%S") + ".txt"
Result_name = os.path.dirname(__file__) + "/Data/Result.txt"
print("Save file: " ,Data_name)
with open(Data_name, 'w') as f:
    while z == 0:
        D = int(input("How many lists in number(2~):"))
        if D <= 1:
            print("DON'T INPUT LOWER THAN 2")
            z = 0
        else:
            z = 1
    print("list length: ",D , file = f)
    print("list length: ",D)

    for i in range(0,D,1):
        list.append(float(random.uniform(-1000,1000)))

    print("Before", file= f)
    print("Before")
    for i in range(D):
        print(list[i], file = f)
        print(list[i])

    i = 0
    I = 0
    k = 0
    temp = 0
    z = 0

    while z == 0:
        mode = input("Up or Down:")
        if mode =="Up" or mode =="Down":
            break
        else:
            print("DON'T INPUT OTHER MODE")
            z = 0
    print("Sort type:", mode, file = f)
    print("Sort type:", mode)

    start = time.time()        
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
            end = time.time()
            time_diff = end - start
            print("time:{:.3f}s".format(time_diff) , file = f)
            print("time:{:.3f}s".format(time_diff))
            print("Count:",I , file = f)
            print("Count:",I)
            break
    print("After", file= f)
    print("After")
    for i in range(D):
        
        print(list[i] ,file = f)
        print(list[i])

with open(Result_name, 'a') as r:
    print(now.strftime("%Y%m%d_%H%M%S"),format(D, "*^11"),format(time_diff, ".3f"),I, sep = ":", file = r)