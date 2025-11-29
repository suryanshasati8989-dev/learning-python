# my_list = ["apple","pineapple","mango","pineapple"]
# property of list

# print(my_list[-1])
# my_list[0]=2
# print(my_list)\

# length of a list
# my_list1 = ['apple','banana','papaya']
# len(my_list)

#practice question 1
# fruits = ['apple','mango','banana']
# fruits[2]='cherry'
# print(fruits)
#2
# fruits[1:3]= 'papaya','coconuts'
# print(fruits)
#3
# 


#4
# number = [10,20,30,40,50]
# number[2]=25,27
# print(number)

#5
# fruits = ['apple','mango','banana']

# fruits[1:3] = ['pear']

# print(fruits)


#PYTHON- ADD LIST ITEMS
#append items (append())
# thislist = ['apple','mango','banana',]
# thislist.append('papaya')
# print(thislist)

#insert items (insert())
# this_list = ['apple','banana','cherry']
# this_list.insert(1,'pineapple')
# print(this_list)

#Extend List(extend())

# ThisList = ['apple','banana','cherry']
# ThisList1 = [1,2,3,4,5]
# ThisList.extend(ThisList1)
# print(ThisList)


#4 

# a = ['a','b','c']
# a.extend('abc')
# print(a)
#5

# insert

# thislist = ['apple','banana','cherry']
# [print(x) for x in thislist]

###remove list item
                              
# remove by Values
# thislist = ['apple','banana','cherry']
# thislist.remove('banana')
# print(thislist)

###
#q1
# fruits = ['mango','banana','cherry']
# [print(x,fruits[x])for x in range(len(fruits))]

##q2
# fruits = ['mango','banana','cherry']
# for i in fruits:
#     print(i.upper())


# ##q3
# world = ['apple','banana','avocado','cherry','apricot']
# a = []
# for x in world:
#     if x.startswith('a'):
#         a.append(x)
# print(a)


###4
# numbers = [1,2,3,4,5,6,7,8]
# for i in numbers:
#     if i%2==0:
#         print(i)
#     else:
#         continue


# nums = [10,20,30,40]
# sum = int()
# for i in nums:
#     a=i
#     sum=a+sum
# print(sum)


# ##6
# nums = [10,20,30,40]
# nums.sort()
# print(nums[-1])

###7
# nums = [10,20,30,40]
# a=[]
# # nums.reverse()
# for i in nums[-1::-1]:
#     a.append(i)
#     print(a)


###8



###9
# nums = [10,20,30,40]
# x=[]
# for i in nums:
#     x.append(i*i)
# print(x)


###10
# nums = [10,20,30,40,100]
# for i in nums:
#     if i>50:
#         print(i)
#     else:
#         continue

###11
# nums = [10,20,30,40,3,4,5,6,78,]
# [print(i)for i in nums if i%2!=0 ]

###12                                                            nahi bana
# fruits=['apple','banana','apple','cherry','mango']
# j=[]
# for i in fruits:
#     if i!='apple':
#         continue
#     else:
#       j.append(i)
# print(len(j))

###13
# fruits=['apple','banana','apple','cherry','mango']
# for i in fruits[0::2]:
#     print(i)

###14

# fruits=['appe','nana','aple','cherry','mango']
# for i in fruits[1::2]:
#     if len(i)>5:
#         print(i)
#     else:
#         continue
fruits=['appe','nana','aple','cherry','mango']
for i in fruits:

    print(fruits.count())



