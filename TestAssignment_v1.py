#!/usr/bin/python
import os

user_path = os.getcwd()
print("Current dir %s" % user_path)

user_path = input("path -> ")
os.chdir(user_path)

user_path = os.getcwd()
print("Dir: %s" % user_path)

user_file = input("file -> ")
print("File: %s" % user_file)
f = open(user_file)
theline = f.readline()
for line in f.readlines():
    print(line, end='')
l = len(theline)
m = 0
ind = 0
count = 0
for i in range(l):
    if theline[i] != ' ':
        count += 1
    else:
        if count > m:
            m = count
            ind = i - count
        count = 0
if count > m:
    m = count
    ind = i - count + 1
print('longest word:',theline[ind:ind + m])

