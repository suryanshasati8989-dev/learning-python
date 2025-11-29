# tuple = ('raman',"kamlash",23,45,76)
# print(type(tuple))
# for i in tuple:
#     print(i)

# if 'rman' in tuple:
#     print("yes")

# print(tuple[1:4])


#PYTHON TUPLE : ACCESSING ITEMS

#INDEXING(POSITIVE)
# Thistuple = ('apple','banana','cherry')
# print(Thistuple[2])

#INDEXING(indexing)
# Thistuple = ('apple','banana','cherry')
# print(Thistuple[-2])

# Range of indexes(Slicing)
# t = ('a','b','c','d','e','f')
# print(t[2:5])

#range of negative indexing
# t = ('a','b','c','d','e','f')
# print(t[::-1])

#check if item exists
# t = ('a','b','c','d','e','f')
# if 'a'in t:
#     print("yes")

# python tuple values
t = ('a','b','c','d','e','f')
l = list(t)
l[1]='er'
t = tuple(l)
print(l)

