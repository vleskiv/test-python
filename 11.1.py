import re
mylist=list()
handle = open("regex_sum_220041.txt")
for line in handle:
    line=line.rstrip()
    y=re.findall('[0-9]+', line)
    if len(y) >= 1:
        mylist.extend(y)
myint=[int(i) for i in mylist]
print ( sum(myint) )