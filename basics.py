###############################################################################

print("Hi from python")

###############################################################################

food = input("What do you like to eat? ")
print(food + " seems yummy.")

###############################################################################

name = input("What's your name? ")

if name == 'Kapil':
    print(name + " is really lazy")
else:
    print(name + " works hard! " + name + " plays harder!")

###############################################################################

name2 = input("What's your name? ")

if name2 == 'Kapil':
    print("{} is really lazy".format(name2))
else:
    print("{} works hard! {} plays harder!".format(name2, name2))

###############################################################################

inputSting = input("What string to repeat? ")
inputInt = input("How many times to repeat? ")

print(inputSting*int(inputInt))

###############################################################################

user_string = input("What's your string? ")
user_num = input("What's your number? ")

try:
    our_num = int(user_num)
except:
    our_num = float(user_num)

if not '.' in user_num:
    print(user_string[our_num])
else:
    ratio = round(len(user_string)*our_num)
    print(user_string[ratio])

###############################################################################

my_list = [1, 2.5, 'a']
print(len(my_list))
print(my_list[2])

list('a')
print(list)
list('hello')
print(list)

hello_list = list('hello')
check = 'e' in hello_list
print(check)
check = 'k' in hello_list
print(check)

sentence = "My name is Khan! and I'm not a terrorist!"
print(sentence.split())

sentence_list = sentence.split()
new_sent =  '_'.join(sentence_list)
print(new_sent)
new_sent =  ' '.join(sentence_list)
print(new_sent)

###############################################################################

def say_hello():
    print("Hello World!")

def times_ten(num):
    print(num*10)

def square(num):
    return num*num

ans = square(5)
print(ans)

###############################################################################