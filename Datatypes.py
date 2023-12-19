a = "Hello World"
print(a[0:5])
#output - Hello

# a = "Hello World"
# print(a[6])
# #output - w

# print(a*3)
#output = hellow world 3 times.


#list[]
ice_cream = ['Vanilla',3,['scoops','spoon'],True]
ice_cream.append('Salted caramel')#adds at the end of the list
print(ice_cream)
print(len(ice_cream))

ice_cream[0]= 'chocolate'
print(ice_cream)

# to see the list with in the list first use the main index then the inner index
print(ice_cream[2][0])


#tuple- immutable
tuple_scoops = (1,2,3,4 )

#set- no duplicate values(only prints out the unique values automatically), no indexes - best to you for loop
daily_pints = {1,2,3}
killer_dailypintslog= {4,5,6,1,2,3,}
print(daily_pints | killer_dailypintslog) # note the | is to print out the unique in  two sets

print(daily_pints & killer_dailypintslog) # note the & is to print out the duplicate in two sets

print(daily_pints - killer_dailypintslog) # note the - is to print out what doesn't match

print(killer_dailypintslog - daily_pints) # note the - is to print out what

print(daily_pints ^ killer_dailypintslog) # note the ^ is to print out what is in one or the other but not both

#dictionaries
# key value pair
dict_cream= { 'name': 'Alex Fredberg','weekly intake':5,'favorite_icecream':['mc','chocolate']}
print(dict_cream)
print(dict_cream.values())
print(dict_cream.keys())
print(dict_cream.items())

#calling a key
print(dict_cream['name'])
#output - Alex Fredberg

#updating a key
dict_cream['name']= 'christine Fredberg'
print(dict_cream['name'])

#updating the whole thing
# it won't delete anything
dict_cream.update({ 'name': 'Alex Fredberg','weekly intake':5,'weight':300})
print(dict_cream)

# deleting a key with value# take note no brackets
del dict_cream['weight']
# https://www.youtube.com/watch?v=lPVke-p4S7s&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=45

#logical operators and , or not - returns false if the  result is true















