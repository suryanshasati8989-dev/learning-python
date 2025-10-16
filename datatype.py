#
# fruits = ["apple","pineapple","mango",]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(fruits[1:2])
# fruits[0]="kiwi"
# print(fruits)
# fruits.append("babnana")
# print(fruits)

# #tuple
# '''tuple = ("ram","sita","hanuman")
# print(tuple)
# print(tuple[0])
# print(len(tuple))
# tuple[0]="radha"
# R = range(7)
# print(R)'''

# #Dictanary

# person = {"ram":"sita","krishna":"radha",}
# print(person)
# print(person["ram"])

# #sets

# set = {12,"suryansh","divyansh",12,34,-12}
# print(set)
# set = frozenset([12,34,56,"yesh"])
# print(set)
# print(10<2)

# #string

# a="hellow world#"
# print(a[2:5])

# for x in "banana":
#     print(x)

# print(len(a))
# a = " My Name , Is Ram And ,A am studying       "
# print("the" not in a)

# #Slicing

# print(a[2:7])
# print(a[2:12:2])
# print(a[14:1:-1])
# print(a.split(",")
# fruits = ["apple","pineapple","mango",]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(fruits[1:2])
# fruits[0]="kiwi"
# print(fruits)
# fruits.append("babnana")
# print(fruits)

# #tuple
# '''tuple = ("ram","sita","hanuman")
# print(tuple)
# print(tuple[0])
# print(len(tuple))
# tuple[0]="radha"
# R = range(7)
# print(R)'''

# #Dictanary

# person = {"ram":"sita","krishna":"radha",}
# print(person)
# print(person["ram"])

# #sets

# set = {12,"suryansh","divyansh",12,34,-12}
# print(set)
# set = frozenset([12,34,56,"yesh"])
# print(set)
# print(10<2)

# #string

# a="hellow world#"
# print(a[2:5])

# for x in "banana":
#     print(x)

# print(len(a))
# a = " My Name , Is Ram And ,A am studying       "
# print("the" not in a)

# #Slicing

# print(a[2:7])
# print(a[2:12:2])
# print(a[14:1:-1])
# print(a.split(","))


# for i in range(1,6):
#     print(i*i)
# a = int(input("enter number"))

# for i in range(0,a,2):
#      print(i)
    
# a = int(input("enter number "))
# for i in range(1,a+1):
#      print(i*2)

# i=1
# a = int(input("enter your no :"))
# while i <= a:
#     print(i*2)
#     i+=1
     

# i=1
# a = int(input("enter your no :"))
# while i <= a:
#     print((i*2)-1)
#     i+=1

# a = int(input("enter number "))
# for i in range(1,a+1):
#      print((i*2)-1)
# sum=0
# a = int(input("enter your no:"))
# for i in range(1,a+1):
#     sum+=i
# print(sum)

# sum = 0
# a = int(input("enter your no:"))
# while 0 <= a:
#     sum+=1
# print(summ)


# a = int(input('enter your no:'))35
# rev = 0
# while a>0:
#     digit = a%10  d=3
#     rev = rev*10 + digit   r=5*10+3
#     a=a//10   a=0
# print(rev)

    

# a = int(input("enter your no:"))
# a = str(a)
# rev = 0
# for i in a:
#     a=int(a)
#     digit = a%10
#     rev = rev*10 + digit
#     a=a//10
# print(rev)

# sum=0
# a = int(input("enter your no:"))
# for i in range(1,a+1):
#     sum+=i
# print(sum)
########

# n = int(input("enter your no"))
# a,b=0,1
# count = 0

# while count<=n:
#     print(a,end=" ")
#     nextterm = a+b
#     a=b
#     b=nextterm
#     count+=1

# n= int(input("enter your no"))
# a,b=0,1
# for i in range(n):
#     print(a,end=" ")
#     nextterm = a+b
#     a=b
#     b=nextterm


# a = int(input('enter your no '))
# b = int(input('enter your 2nd no '))
# for i in range(a,b+1):
#     print(a)
#     if(i%1==0 and i%i==0):
#         print()
#     else:
#         continue 


# a = int(input("enter your no:"))
# sum=0
# while a>0:
#     digit = a%10
#     sum+=digit
#     a=a//10
# # print(sum)

# a = input('enter your no')
# sum = 0
# for i in a:
#     digit = int(a)%10
#     sum+=digit
#     a=int(a)//10
# print(sum)

# a = int(input("enter your no 1st:"))
# b = int(input("enter your no 2nd no:"))
# for i in range(a,b+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                break
#         else:
#             print(f'your all prime no is{i}')



# a = int(input("enter your no:"))
# orignal = a
# rev = 0

# for i in a:

#     digit = a%10
#     rev = rev*10 + digit
#     a=a//10
#     if rev == orignal:
#         print("palendrom no")
                             

# a = int(input("enter your no:"))

# sum=0

# while  a> 0:
#     digit = a%10
#     sum += digit 
#     a = a//10
# print(sum)


# num = int(input("enter your no"))
# orignal_no = num
# sum = 0
# length = len(str(num))
# while num > 0:
#     digit=num%10
#     sum+=digit**length
#     num=num//10
# print(sum)

# if (sum == orignal_no):
#     print('armstrong no ',sum)
# else:
#     print("not a armstrong")


num = (input("enter your no"))
orignal_no = num
sum = 0
length = len(str(num))
for i in num:
    num = int(num)
    digit = i%10
    sum+=digit**len(str(num))
    num=num//10
print(sum)



