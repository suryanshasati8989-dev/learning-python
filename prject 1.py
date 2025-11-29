# import random
# option = ('rock','paper','scisser')
# player=()
# computer = random.choice(option)


# while player not in option:
#     player = input('enter a choice(rock,paper,scissor):')

# print(f'player:{player}')
# print(f'computer:{computer}')

# if(player==computer):
#     print('its tie')
# elif(computer=="rock"and player=="scisser" or computer=="paper"and player=="rock" or computer=="scissor"and player=="paper"):
#     print('computer win')
# else:
#     print('player win')



###########python project 2

# fine the menu of restaurant
menu = {
    'pizza':40,
    'burger':50,
    'noodles':60,
    "coffe":80
}

#greeting

print('welcome sir this is our menu')
print("pizza:40","burger:50","noodles:60","coffe:80")

order_total = 0
item_1 = input('enter the name of item which you want to order=')
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1}is added to your order")
else:
    print("not avilable")
another_order= input("do you want to add another item to your list? (yes/no)")

if another_order == "yes":
    item_2 = input('enter the name of item which you want to order=')
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"your item {item_2}is added to your order")
    else:
        print("not avilable")
print(f"the total amount of item is {order_total}")








