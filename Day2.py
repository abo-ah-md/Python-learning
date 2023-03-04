## IF conditions 
## IF can be used in multiple ways as follows 
## the initial structure if "condition" : "start the the following"" 

#number = 5
## note that python can be senstive to indintation 
#if number < 6 :
#    print(number)

## note that python can be senstive to indintation 
#for example this make an error
#if number >0:
#   print(number)

#else usage 
##if number < 6 :
##    print(number)
##else:
#    print("more than 6")
    

## Exircise take an input number and if it is even print even and vise versa
##usernumber=input("please enter a nmumber  ")
#if int(usernumber) %2 == 0 :
#    print("even")
#else:
#    print("odd")


## else if in python is written in (elif)

#number= 20

#if number == 19 :
#    print("19")
#elif number<25:
#    print("more than 25")
#else:
#    print("😒")

##Exirsice 
## write a program that enters the user purchasing value and make a discount it will print
#the initial value 
#the discounted amount less than 1000 5% , 1000-5000 10%, more than 5000 15%
#the total after discount 

"""
user_input = int(input("enter the purchase cost"))

print(user_input)

if user_input <1000 :
    user_input_Discount = int((user_input*5)/100)
    print(user_input_Discount)
    print(int(user_input-user_input_Discount))
elif user_input >=1000 & user_input <5000 :
    user_input_Discount = int((user_input*10)/100)
    print(user_input_Discount)
    print(int(user_input-user_input_Discount))
elif user_input> 5000 :
    user_input_Discount = int((user_input*15)/100)
    print(user_input_Discount)
    print(int(user_input-user_input_Discount))
"""
#check if array has the element
""" 
pass_Grade= ["A","B","C","D"]
Fail_Grade=["F"]

user_Grade_input=input("enter your Grade")

if user_Grade_input in pass_Grade :
    print("You have passed")
elif user_Grade_input in Fail_Grade:
    print("You have Failed")
"""

#string has also coule of methods like upper and lower 
"""
pass_Grade= ["A","B","C","D"]
Fail_Grade=["F"]

user_Grade_input=input("enter your Grade").upper()

if user_Grade_input in pass_Grade :
    print("You have passed")
elif user_Grade_input in Fail_Grade:
    print("You have Failed")
    """
    
# you can also make and or condition
"""
number=10

if number == 5 or number == 10 :
    print("yes")
    

if number > 0 and number <11:
    input("right where you want")
    """

#nested if is written in this way 
"""
name = "khalid"

if name != "hamad":
    if name == "khalid":
        name = "hamad"
        print(name)
        """

#loops are iterate in Python in this way 
"""
names=["ahmed","khalid","saad"]

for i in names :
    print(i)
    
    """
#Range is a method in Python that allows you to define a range instead of writing every element

"""
name = "I love Python"
for i in range(11):
     print(name)
"""
"""
numbers =list(range(0,500))
print(numbers)
"""
## while loop

"""
while True:
    number= int(input("what is the off switch"))
    if number == 0 :
        print("thank you")
        break
        """
#for uses else also in python to excute it after the loop is done
"""
name= ["ahmed","sad","pals"]

for i in name:
    print(i)
else:
    print("finished")
    """