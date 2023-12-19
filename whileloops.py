number = 0

# while number <5:
#     print(number, end=",")
#     number+=1

#break
# while number <5:
#     print(number, end=",")
#     if number == 3:
#         break
#     number+=1

#else
# while number <5:
#     print(number, end=",")
#     if number == 6:
#         break
#     number+=1
# else:
#     print('No longer <5')

#continue will go to the next iteration in the loop
# while number <5:
#     print(number, end=",")
#     if number == 3:
#         continue
#     number+=1
# else:
#     print('No longer <5')

#another example where it will continue
while number <5:
    number += 1

    if number == 3:
        continue
    print(number, end=",")
else:
    print('No longer <5')

    # https: // www.youtube.com / watch?v = ECduJk00mUU & list = PLUaB - 1
#functions
def number_square(number,power):
    print (number**power)

number_square(21,2)


# arbitrary arguments - you can create a blank parameter and later can decide how many
def number_args(*number):# the *number can also be * args it doesn't matter
    print(number[0]*number[1])

number_args(5,6,1,2,8) # the number[0] is 5, the number[1] is 6

# another example
args_tuple = (5,6,1,2,8)

def number_args1(*number):
    print(number[0]*number[1])
number_args1(*args_tuple) # note you need to add * here as well.

# keyword arguements - resassinning the parameters
def number_square(number,power):
    print (number**power)

number_square(power=5,number = 3)

#using the combination of arbitratry and keyword arguements
def number_kwarg(**number): # two ** for the use of both
    print('My number is:'+number['integer'] + 'My other number:'+number['Integer2'])

number_kwarg(integer = '2309', integer2 = '349')



