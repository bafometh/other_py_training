import random
from time import sleep
import numpy

def get_int(num):
    while True:
        try:
            i = int(input(num))
            z = i
            return i


        except ValueError as err:
            print(err)

num = get_int("введите число: ")
print("ввели число ", num)
rand_num =  random.randint(1,50)
print("случайное чило ", rand_num)

sleep(5)
#numpy.random.rand(1,5)
country = ["ukraine", "russia", "germany", "spain"]

if rand_num  > num :
    while rand_num  > num:
        print("страны ", country)
        print(num)
        num += 1
elif num >= rand_num:
        print("число больше или равно")
