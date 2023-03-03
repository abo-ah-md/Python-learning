from datetime import datetime,date
print("Hello World")

#dynamic typed language  x= 0
# case sencitive name != Name


#we use type() to know the variable type
#print(type(1.2))
#print(type("sound"))
#print(type(1))
#print(type(True))

# can define more than one variable in a single statment 
# a,b,c = 15,35,49

#to get the user input 
#Name=input("please enter your name")
#print(Name)

#to cast a variable type 
#year= int(input("please enter your birth year"))


#import datetime // to import libraries
#from datetime import * //  to import certain element from libraries

########################################################
#Exercie
## Get the user age by there birth date




#year= int(input("please enter your birth year"))

#month= int(input("please enter your birth month"))

#day= int(input("please enter your birth day"))

#dob = datetime(year,month,day)
#today_date = datetime.now()
#user_dob= int(int(( today_date - dob ).days)/365)


#print(user_dob)
################################

#to get the length of a string
#print(len("hi"))

#to print from certain index to another
#greeting = "hi Ahmed"
#print(greeting[3:10])


##########################################################
# Array list  are defined in this way

#Names_list = ["ahemd","Khalid",27,50]
##print(Names_list[0])

## or to print from -- to -- // [index starting point:how many after starting point ]
##print(Names_list[0:2])

#To add to the array we use Append

#Names_list.append("hussam")
#print(Names_list)

# to change on an element in an array 
#Names_list[0]="Abdullah"
#print(Names_list)




##############################################################################################
#Tuples are data structure like arrays list  but does not change its value because it is consedered immutable


#my_coordanates =(245,5546,265);



#this will make an error ⛔ 
#my_coordanates[0]=1

#in addition you can isert in as 2 dimentions array
# but the rule still the same in regard of not being able to change the tuple value after assigning
#my_coordanates_list = [my_coordanates,(2455,444,2655),(24445,566546,28865)]
#print(my_coordanates_list[0][1])


## Dictionary 
#Dictionaries are also data structure type that is like objects in Javascript meaning key:value pairs

api_Json_Example= {"name":"abdullah",
                   "age":25}
print(api_Json_Example["name"])
#or
print(api_Json_Example.get("name"))


##changing values 
api_Json_Example["name"]= "mohammed"
print(api_Json_Example["name"])

##adding new entry
api_Json_Example["Grade"]="B"
print(api_Json_Example["Grade"]) 




