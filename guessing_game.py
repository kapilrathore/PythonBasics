import random

print("Guess the random number from 1 to 10! ")

rand_num = random.randint(1,10)
chances = 0

def guess_num():
    user_num = input("Your guess: ")
    our_num = int(user_num)
    return our_num

while True:
    print("You have {} chances".format(3 - chances))

    if chances == 3:
        print("Chances over! It was {}".format(rand_num))
        break

    guess = guess_num()

    if guess == rand_num:
        print("Right guess! It is {}".format(rand_num))
        break
    elif guess > rand_num:
        print("A bit less!")
    elif guess < rand_num:
        print("A bit more!")

    chances += 1