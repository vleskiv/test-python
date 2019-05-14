
# show part of a string
fruit[1:4]
fruit[position-start:position-end]
# String lenght
len()
letter operator
if 'a' on fruit:
# Object method
zap=mystring.lower()
print('Hi there'.lower())
str.upper str.lower
str.capitalize()
str.replace()
# Seaarching position of string 'na' in var 'fruit'
fruit.find('na',3) # where 3 - means find 'na' after 3d position
fruit.startswith('bana')
# Replace all matches
fruit.replace('banana','apple')
# Striping whitespace
strip() lstrip() rstrip()
# find and print part of string
text = "X-DSPAM-Confidence:    0.8475";
numstr=text.find('0.')
num=float(text[numstr:numstr+6])
print(num)
# open file for read
text=open("romeo.txt", "r") (for - use per-line iteration)
string=text.read()
# Find specific line in file
for line in text:
    line = line.rstrip
    if line.startswith('From:')
# OR
    if not line.startswith('From:'):
        continue
    print(line)
# search string in lines
    if '@gmail.com' in line:

# exit form the program right now:
quit()

## try/except: 
# Simple check if value is integer
while True:
    try:
        count = input('Enter count: ')
        int(count)
    except ValueError:
        print('error')
        continue
    else:
        count=int(count)
        break

# Function: check if value is positive integer
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, value must be integer")
            continue
        if value < 0:
            print("Sorry, value must not be negative.")
            continue
        else:
            break
    return value
# Input from user
count = get_non_negative_int("Enter count: ")
position = get_non_negative_int("Enter position: ")


#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#Sample file: http://www.py4e.com/code3/mbox-short.txt
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
c=0
all=float(0)
list = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    twodots=line.find(':')
    value=float(line[twodots+1:twodots+8])
    all=all+value
    c=c+1
print("Average spam confidence:", all/c)

#Variables is not mutable - you can't change one letter in variable, but you can make a copy
#Lists are mutable - so you can change any element of list directly

range(4) # порахує від 0 до 4 і видасть елемент типу list
# Countable loop
for i in range(len(list)-1):
    element=list[i]
    print(element)
# list
mylist=list()
mylist.append(99)
mylist.append('book')
# check if value present in list
20 in list # True/False
mylist.sort()
mylist=string.split() # converl string to list. You can set delimiter in scopes


#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
strlist = list()
for line in fh:
    strlist=line.split()
    for i in range(len(strlist)):
       if strlist[i] in lst:
            continue
       lst.append(strlist[i])
lst.sort()          
print(lst)

# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
strlist = list()
for line in fh:
    if line.startswith('From '):
        strlist = line.split()
        print(strlist[1])
        count=count+1
print("There were", count, "lines in the file with From as the first word")

# Dictionary (key/value)
db=dict()
db['money']=12
print(db['money'])
x=db.get(money, 0) 
# Dictionary counting
counts=dict()
names=['csev','cwen','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)
# List dictionary methods:
mydict.keys()
mydict.values()
mydict.items()
# Two-iteration variables are best practice:
for aaa,bbb in db.items():
    print (aaa,bbb)
# Instead this, because we use name 'db' two times in code:
for key in db.keys():
    print (key, db[key])

# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails=dict()
for line in handle:
    line=line.rstrip()
    lst=line.split()
    if len(lst)>2 and lst[0]=='From':
        key=lst[1]
        mails[key]=mails.get(key,0)+1
count=-1
for k,v in mails.items():
    if count < v:
        count=v
        email=k
print (email, count)

# tuple=list, but not mutable. more efficient in memory and performance. Good for temp vars
x=(4, 'book', 5) # create new tuple with 3 elements
mydict.items() # return a list of two-element tuples
# Double assignment
(x,y) =(4,5)

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour
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

# Regular expressions:
import re
re.search() # returns True/Flase
re.findall('<regexp>',mystring) # returns all matches as list
^From.+<symbol> # to-last-matches <symbol> (Greedy)
^From.+?<symbol> # to-first-matches <symbol> (Non-Greedy)
re.findall('^From (\S+@\S+)',x) # Scopes - search "From <email>", but returns only "<email>"
[^ ] # any non-blank character
# Python	Regular	Expression	Quick	Guide
^ Matches the beginning of a line
$ Matches the end of the line
. Matches any character
\s Matches whitespace
\S Matches any non-whitespace character
* Repeats a character zero or more times
*? Repeats a character zero or more times
 (non-greedy)
+ Repeats a character one or more times
+? Repeats a character one or more times
 (non-greedy)
[aeiou] Matches a single character in the listed set
[^XYZ] Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
( Indicates where string extraction is to start
) Indicates where string extraction is to end

# 11.1 Find all numbers in text and print sum
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

# 12.1 Socket

# ASCII
print (ord('h')) # shows decimal ascii code
x=b'abc' # class bytes
x='abc' == x=u'abc' # class str in python 3
data.decode() - decode data from bytes to unicode

# urllib
import urllib.request, urllib.parse, urllib.error
import ssl
handle=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in handle:
    print(line.decode().strip())

## Object, class, method
dir(x) # shows all methods for class (str|float|int|dict) of variable "x". Variabl=Object
# Create and use class, where:
# "party" is method (function in class)
# "x" is attribute (variable in class)
# "PartyAnimal" is class (template)
# "an" is object (a particular instance of a class)
class PartyAnimal:
        x=0
        def party(self):
                self.x=self.x+1
                print("So far",self.x)
an=PartyAnimal()
an.party()
an.party()
an.party()
# Class will be destructed at the end of program or when you manually reassign "an" variable