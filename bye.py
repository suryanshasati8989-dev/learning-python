# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))


# s = "i like python"
# print(s.replace("python","java"))
# print(s)

# sum = f'i have {2*45/56} dollar'
# print(sum)

## escape character

print("my name is \"suryansh asati\"")
# print(a)

#Newline
print('my name is \n\\suryansh asati\\')

#Carriage return
print("my name \r is suryansh")

#Tab
print("my name is \t suryansh asati")

#Backslash
print('my name is \bsuryansh')

#Formfeed
print('suryansh \f asati')



# s = 'Hellow World'
# print(s.upper())
# print(s.lower())
# print(s.swapcase())

# strip()/istrip()/rstrip()

# s="hellow world"
# print(s.strip())
# print(s.replace("hellow","world"))
# print(s.split())
# print(s.find("m"))
# print(s.index("m"))

s = "my name is suryansh asati   "
print(s.startswith('name'))
print(s.endswith("asati"))


print(s.count("is"))
print(s.isdigit())
print("mynameisuryanshasati".isalpha())
print(s.isalnum())
print(s.isspace())

#captalize()
print(s.capitalize())
print(s.title())


# formate()/strings
name = "Alice"
age = 13
print('my name is {} and my age is{}'.format(name,age))
print(f'my name is{name} and my age iis {age}')

