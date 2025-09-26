<<<<<<< HEAD
# to check wether a string is palimdrom or not
# to check wether a year is a leap year or not
# a program which cheaks the chracter type vowel consonent digit spcial chracter 
#MAKE A BASIC CALCULATER 
#programm to reverse the string
#take two string and check wheather they are anagram of each other or not
#even or odd using ends with function and using indexing as well
#write a programm to check if the first and last chracter is same or not


# a = input('enter your string:')
# if(a == a[::-1]):
#     print(a"is palimdrom")
# else:
#     print(a'is not palimdrom')

# a = int(input("enter your year in only 4 digit:"))
# if(a%400==0 or (a%4==0 and a%100!=0)):
#     print(a," is a leap year")
# else:
#     print(a," is not a leap year")


# a = input("enter your value:")
# a.lower
# if a.isalpha():
#     if a in ["a","e","i","o","u"]:
#         print("vowel")

#     else:
#         print("consonent")
# elif a.isdigit():
#     print('digit')
   
# else:
#     print("special chracter")


# a = input("entter your string:")
# print(a[::-1])

# a = float(input("enter your no 1:"))
# b = float(input("enter your no 2:"))
# c = input("enter your operater +,-,*,/ :")
# if(c=="+"):
#     print(a+b)
# elif(c=="-"):
#     print(a-b)
# elif(c=="*"):
#     print(a*b)
# else:
#     print(a/b)


# a = input("enter your name:")
# b = input("enter your 2 name:")
# if(sorted(a) == sorted(b)):
#     print("your name anagram")
# else:
#     print("your name is not anagra)


#even or odd using ends with function and using indexing as well

# a = input("enter your no:")
# b = a[-1]
# if (b in ['0','2','4','6','8']):
#     print("even")
# else:
#     print("odd")

# a = input('enter your no')
# if(a.endswith(("0","2","4","6","8"))):
#     print('even')
# else:
#     print("odd")

# write a programm to check if the first and last chracter is same or not

# a = input('enter your first chrac:')

# c=a[0]
# d=a[-1]
# if(c==d):
#     print('same')
# else:
#     print("not same")


# a = int(input('enter your age:'))
# print('eligible for voteing') if a > 18 else print('not eligible')


# a = int(input('enter your first side of trangle '))
# b= int(input('enter your second side trangle '))
# c= int(input('enter your third side of trangle '))
# if(a+b>c and a+c>b and c+b>a):
   
#     if(a==b  or a==c  or c==b ):
#         print("isosales")
#     elif(a==b and b==c):
#         print("equliterial")
#     elif(a+b>c and b+c>a and c+a>d):
#         print("it is triangle")
#     else:
#         print("scalene")
# else:
#     print("not a trangle")


# PHYTHON MATCH STATEMENT

# month = int(input("enter your month:"))
# day = int(input("enter your no:"))

# match month :
#     case 1 if( day == 1):
#         print("january \n monday")
#     case 2 if( day == 2):
#         print("february \n tuesday")
#     case 3 if( day == 3):
#         print('march \n wednesday')
#     case 4 if( day == 4):
#         print("april \n thusday")
#     case 5 if( day == 5):
#         print('may \n friday')
#     case 6 if( day == 6):
#         print('june \n saturday')
#     case 7 if( day == 7):
#         print('july \n sunday')
#     case 8 if ( day == 8):
#         print("augest \ninvalid day")
#     case 9 if(day == 9):
#         print("sept \ninvalid day")
#     case _:
#         print("your number is invalid")

    # LOOP

# i = 1
# while i < 11:
#     print(i)
#     i+=1

# a=int(input("enter your no:"))
# i=1
# while i<11:
#     print(a,"*",i,"=",a*i)
#     i+=1


# i=2
# while i <= 50:
#     print(i)
#     i+=2

# a = int(input('enter your factorial:'))
# fact = 1
# i = 1 
# while i<=a:
#     fact*=i
    # i+=1 #i=1+i
# print(f'your fact is ',fact)


##loops

# fruits = ['banana',"mango","grapes","cherry"]
# for x in fruits:
#     print(x)
# # # 
# for i in "banana":
#     print(i)

##break statement

# fruits = ['banana',"mango","grapes","cherry"]
# for i in fruits:
#     if i == "grapes":
#         break
#     print(i)

##continue statement

# fruits = ['banana',"mango","grapes","cherry"]
# for i in fruits:
#     if i == "grapes":
#         continue
#     print(i)


##range()function

# for i in range(1,50,2):
#     print(i)


##else for loop

# for i in range(4):
#     print(i)
# else:
#     print("its over")

# color = ["red", 'blue', 'purple']
# fruit = ['mango', 'banana', 'pineapple']
# for x in color:
#     for y in fruit:
#         print(x,y)


##pass statement

# for x in range(5):
#     pass

# for i in range(11):
#     print(i)

# a = int(input("enter your no:"))
# for i in range(11):
#     print(a,"*",i,"=",a*i)


# a = int(input('enter your factorial:'))
# fact = 1
# i = 1 
# while i<=a:
#     fact*=i
    # i+=1 #i=1+i
# print(f'your fact is ',fact)



# a = int(input("enter your no:"))
# fact = 1 
# for i in range(1,a+1):
#     fact*=i
# print(f'fact of {i} is { fact}')


a = int(input("enter your no"))
for i in range(1,11):
    print(f'{i} * {a} = {a*i}')
=======
# to check wether a string is palimdrom or not
# to check wether a year is a leap year or not
# a program which cheaks the chracter type vowel consonent digit spcial chracter 
#MAKE A BASIC CALCULATER 
#programm to reverse the string
#take two string and check wheather they are anagram of each other or not
#even or odd using ends with function and using indexing as well
#write a programm to check if the first and last chracter is same or not


# a = input('enter your string:')
# if(a == a[::-1]):
#     print(a"is palimdrom")
# else:
#     print(a'is not palimdrom')

# a = int(input("enter your year in only 4 digit:"))
# if(a%400==0 or (a%4==0 and a%100!=0)):
#     print(a," is a leap year")
# else:
#     print(a," is not a leap year")


# a = input("enter your value:")
# a.lower
# if a.isalpha():
#     if a in ["a","e","i","o","u"]:
#         print("vowel")

#     else:
#         print("consonent")
# elif a.isdigit():
#     print('digit')
   
# else:
#     print("special chracter")


# a = input("entter your string:")
# print(a[::-1])

# a = float(input("enter your no 1:"))
# b = float(input("enter your no 2:"))
# c = input("enter your operater +,-,*,/ :")
# if(c=="+"):
#     print(a+b)
# elif(c=="-"):
#     print(a-b)
# elif(c=="*"):
#     print(a*b)
# else:
#     print(a/b)


# a = input("enter your name:")
# b = input("enter your 2 name:")
# if(sorted(a) == sorted(b)):
#     print("your name anagram")
# else:
#     print("your name is not anagra)


#even or odd using ends with function and using indexing as well

# a = input("enter your no:")
# b = a[-1]
# if (b in ['0','2','4','6','8']):
#     print("even")
# else:
#     print("odd")

# a = input('enter your no')
# if(a.endswith(("0","2","4","6","8"))):
#     print('even')
# else:
#     print("odd")

# write a programm to check if the first and last chracter is same or not

# a = input('enter your first chrac:')

# c=a[0]
# d=a[-1]
# if(c==d):
#     print('same')
# else:
#     print("not same")


# a = int(input('enter your age:'))
# print('eligible for voteing') if a > 18 else print('not eligible')


# a = int(input('enter your first side of trangle '))
# b= int(input('enter your second side trangle '))
# c= int(input('enter your third side of trangle '))
# if(a+b>c and a+c>b and c+b>a):
   
#     if(a==b  or a==c  or c==b ):
#         print("isosales")
#     elif(a==b and b==c):
#         print("equliterial")
#     elif(a+b>c and b+c>a and c+a>d):
#         print("it is triangle")
#     else:
#         print("scalene")
# else:
#     print("not a trangle")


# PHYTHON MATCH STATEMENT

# month = int(input("enter your month:"))
# day = int(input("enter your no:"))

# match month :
#     case 1 if( day == 1):
#         print("january \n monday")
#     case 2 if( day == 2):
#         print("february \n tuesday")
#     case 3 if( day == 3):
#         print('march \n wednesday')
#     case 4 if( day == 4):
#         print("april \n thusday")
#     case 5 if( day == 5):
#         print('may \n friday')
#     case 6 if( day == 6):
#         print('june \n saturday')
#     case 7 if( day == 7):
#         print('july \n sunday')
#     case 8 if ( day == 8):
#         print("augest \ninvalid day")
#     case 9 if(day == 9):
#         print("sept \ninvalid day")
#     case _:
#         print("your number is invalid")

    # LOOP

# i = 1
# while i < 11:
#     print(i)
#     i+=1

# i=5
# while i <= 50:
#     print(i)
#     i+=5

i=2
while i <= 50:
    print(i)
    i+=2
>>>>>>> 067572088bd55165fa8965244f0aa9849853a61b
