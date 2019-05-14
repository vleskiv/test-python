name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time=dict()
for line in handle:
    if line.startswith('From '):
        line=line.rstrip()
        lst=line.split()
        timestamp=lst[5]
        timestamp_list=timestamp.split(':')
        key=timestamp_list[0]
        time[key]=time.get(key,0)+1
# Sort in k,v order (by key)
for k,v in sorted(time.items()):
    print (k,v)
# Sort in v,k order (by value)
tmp = list()
for k,v in time.items():
    newtuple=(v,k)
    tmp.append(newtuple)
tmp = sorted(tmp)
for v,k in tmp:
    print (v,k)
# Sort in v,k order (by value) - in one line
for x,y in sorted( [ (v,k) for k,v in time.items() ] ) :
    print (x,y)

