import random
from time import sleep
import numpy
#
def get_int(num):
    while True:
        try:
            i = int(input(num))
            z = i
            return i


        except ValueError as err:
            print(err)

num = get_int("enter number: ")
print("your entered number is ", num)
rand_num =  random.randint(1,50)
print("random number ", rand_num)

sleep(5)
#numpy.random.rand(1,5)
country = ["ukraine", "russia", "germany", "spain"]

if rand_num  > num :
    while rand_num  > num:
        print("country ", country)
        print(num)
        num += 1
elif num >= rand_num:
        print("your number bigger or equally")
