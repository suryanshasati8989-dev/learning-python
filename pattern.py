# a = int(input("enter row:"))

# for i in range(a):
#     for j in range(a):
#         print("*",end=" ")

#     print()

# a = int(input("enter row:"))
# for i in range(1,a+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
 

# a = int(input("enter row"))
# for i in range(a,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print( ) 
        
# a = int(input("enter row"))
# for i in range(1,a+1):
#     print(" "*(a-i),end=" ")
#     print("*"*(2*i-1))
#      *
#     ***
#    *****
#   *******
#  *********
        
# a = int(input("enter row"))
# for i in range(a,0,-1):
#     print(" "*(a-i),end=" ")
#     print("*"*(2*i-1))

# *********
#   *******
#    *****
#     ***
#      *

# a = int(input("enter row"))
# for i in range(1,a+1):
#     print(" "*(a-i),end=" ")
#     print("*"*i)


# a = int(input("enter row:"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# 1   
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# a = int(input("enter row:"))
# for i in range(a,0,-1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print( )

# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# a = int(input("enter your no"))
# for i in range(a,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2
# 1



# a = int(input("enter your no"))
# for i in range(1,a+1):
#     for j in range(65,65+i):
#         print(chr(j),end=" ")
#     print()
# A 
# A B
# A B C
# A B C D
# A B C D E

# a = int(input("enmter your no"))
# for i in range(a,0,-1):
#     for j in range(65,65+i):
#         print(chr(j),end=" ")
#     print()

# A B C D E 
# A B C D
# A B C
# A B
# A



# num = 1
# a = int(input("enter no of rows"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(num, end = ' ')
#         num+=1
#     print()



# a = int(input('enter no of rows'))

# for i in range(1,a+1):
#     print(" "*(a-i),end=" ")
#     print("*"*(2*i-1))
# for j in range(a,0,-1):
#     print(" "*(a-j),end=" ")
#     print('*'*(2*j-1))


#      *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *

# a = int(input("enter no of row"))
# for i in range(a,0,-1):
#     print(" "*(a-i),end=" ")
#     print("*"*(2*i-1))
# for j in range(1,a+1):
#     print(" "*(a-j),end=" ")
#     print("*"*(2*j-1))

#  *********
#   *******
#    *****
#     ***
#      *
#      *
#     ***
#    *****
#   *******
#  *********

# n = int(input('enter your row:')) 
# for i in range(1,n+1):
#     a= "*"*i
#     b= " "*(2*(n-i))  
#     c= "*"*i
#     print(a+b+c)   
# for i in range(n,0,-1):
#     a= "*"*i
    
#     b= " "*(2*(n-i))  
#     c= "*"*i
#     print(a+b+c)   

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# a= int(input("enter row")) 
# for i in range(1,a+1):
#     if i==1 or i==a:
#         print("*"*a)
#     else:
#         print("*"+" "*(a-2)+"*")
    
# *****
# *   *
# *   *
# *   *
# *****
        
# a = int(input("enter row"))
# for i in range(1,a+1):
#      print(" "*(a-i),end=' ')
#      if(i==a):
#         print('*'*(2*i-1))
#      elif(i==1):
#         print("*")
#      else:
#         print("*"+" "*(2*i-3)+"*")

#      *
#     * *
#    *   *
#   *     *
#  *********


# a = int(input("enter row"))
# for i in range(a,0,-1):
#      print(" "*(a-i),end=' ')
#      if(i==a):
#         print('*'*(2*i-1))
#      elif(i==1):
#         print("*")
#      else:
#         print("*"+" "*(2*i-3)+"*")
#  *********
#   *     *
#    *   *
#     * *
#      *


# a = int(input("enter row"))
# for i in range(1,a):
#      print(" "*(a-i),end=' ')
#      if(i==a):
#         print('*'*(2*i-1))
#      elif(i==1):
#         print("*")
#      else:
#         print("*"+" "*(2*i-3)+"*")
# for i in range(a-1,0,-1):
#      print(" "*(a-i),end=' ')
#      if(i==a):
#         print('*'*(2*i-1))
#      elif(i==1):
#         print("*")
#      else:
#         print("*"+" "*(2*i-3)+"*")


#      *
#     * *
#    *   *
#   *     *
#   *     *
#    *   *
#     * *
#      *

# a = int(input("enter row"))
# for i in range(a-1,1,-1):
#      print(" "*(a-i),end=' ')
#      if(i==a):
#         print('*'*(2*i-1))
#      elif(i==1):
#         print("*")
#      else:
#         print("*"+" "*(2*i-3)+"*")
# for i in range(1,a):
#      print(" "*(a-i),end=' ')
#      if(i==a):
#         print('*'*(2*i-1))
#      elif(i==1):
#         print("*")
#      else:
#         print("*"+" "*(2*i-3)+"*")

# a = int(input("enter your row :"))
# for i in range(0,a+1):                   
#     if i==1 or i==a:
#         print("*"*n)
#     else:
























        
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
