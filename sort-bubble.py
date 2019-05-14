mylist=[4, 3, 5, 2, 1, 6, 0, 7]
a = len(mylist)
count=0
for x in range(a):
    for y in range(0, a-x-1):
        if mylist[y] > mylist[y+1]:
            mylist[y], mylist[y+1] = mylist[y+1], mylist[y]
        count=count+1
print (mylist)
print ('Operations:', count)