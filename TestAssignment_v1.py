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
theline = f.read()
listWords = theline.split()
lword=len(listWords)
letter=len(theline)
lletter=letter-1

idLongestWord = 0
idshortestWord = 0

for i in range(1,len(listWords)):
    if len(listWords[idLongestWord]) < len(listWords[i]):
        idLongestWord = i

    else:
        if len(listWords[idshortestWord]) > len(listWords[i]):
            idshortestWord = i

average=(lletter / len(listWords))
lmax = len(listWords[idLongestWord])
lmin = len(listWords[idshortestWord])
print(theline)
print('max: ',listWords[idLongestWord],' len: ',lmax, '\nMin: ',listWords[idshortestWord],' len: ',lmin,'\nWords: ', lword,'\nletter: ', lletter,' \nAverage :',average )








