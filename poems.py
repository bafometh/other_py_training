import random

art = ["the", "a", "of", "on", "and"]
su = ["cat", "dog", "woman", "man","people"]
gla = ["sang", "ran", "seen", "been", "jump"]
nar = ["loudly", "quietly", "well", "badly", "happily"]


def get_int(num):
    while True:
        try:
            i = int(input(num))
            z = i
            return i
        except ValueError as err:
            print(err)

num = get_int("length: ")

while num != 0 :
    print(random.choice(su) + " " + random.choice(art) + " " + random.choice(gla) + " " + random.choice(nar) + "\n")
    num -= 1

