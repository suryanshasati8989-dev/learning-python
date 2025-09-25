fruits = ["apple","pineapple","mango",]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:2])
fruits[0]="kiwi"
print(fruits)
fruits.append("babnana")
print(fruits)

#tuple
'''tuple = ("ram","sita","hanuman")
print(tuple)
print(tuple[0])
print(len(tuple))
tuple[0]="radha"
R = range(7)
print(R)'''

#Dictanary

person = {"ram":"sita","krishna":"radha",}
print(person)
print(person["ram"])

#sets

set = {12,"suryansh","divyansh",12,34,-12}
print(set)
set = frozenset([12,34,56,"yesh"])
print(set)
print(10<2)

#string

a="hellow world#"
print(a[2:5])

for x in "banana":
    print(x)

print(len(a))
a = " My Name , Is Ram And ,A am studying       "
print("the" not in a)

#Slicing

print(a[2:7])
print(a[2:12:2])
print(a[14:1:-1])
print(a.split(","))
