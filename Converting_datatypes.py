num_int = 7
num_str = '7'

conver= int(num_str)
print(type (conver))

list_type = [1,2,3]
list_tuple = tuple(list_type)

# note for set - it only takes in unique values no duplicates
dict_type = {'name':'Alex', 'age':'21'}
# now to take all of the keys and put it into a list
print(list(dict_type.keys()))


# converting string to list - see what happens
long_str= 'I like to party'
print(list(long_str))
#output - ['I', ' ', 'l', 'i', 'k', 'e', ' ', 't', 'o', ' ', 'p', 'a', 'r', 't', '

