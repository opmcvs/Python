#https://www.youtube.com/watch?v=-BOBedcjySI&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=46
if 25 > 10:
    print('It works.')

# one liner
print('It worked.') if 10>30 else print('it did not work')


#for loops
#https://www.youtube.com/watch?v=zmIdC0_0BgY&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=47

integers = [1,2,3,4,5]
for number in integers:
    print(number)
    print(number,end=',')

for number in integers:
    print("Hail to the king")

ice_cream_dict = { 'name': 'Alex Fredberg','weekly intake':5,'favorite ice cream':['MCC','chocolate']}

for cream in ice_cream_dict.values():
    print(cream,end= ',')

for cream in ice_cream_dict.items():
    print(cream)

for key,value in ice_cream_dict.items():
    print(key,'->',value)


# nested for loops
flavors = ['vanilla','chocolate','cookie dough']
toppings = ['Hot fudge','Oreos','Marshmallows','strwbery']

for one in flavors:
    for two in toppings:
        print(one,'topped with',two)
        # https: // www.youtube.com / watch?v = zmIdC0_0BgY & t = 8s
















