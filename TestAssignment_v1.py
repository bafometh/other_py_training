#!/usr/bin/python
import os

user_path = os.getcwd()
print("Current dir %s" % user_path)

user_path = input("path -> ")
os.chdir(user_path)

user_path = os.getcwd()
print("Current dir %s" % user_path)

