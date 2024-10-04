#logical operator
#================================
#and
print(True and True)
print(3>2 and 34<4)
#or
print(True or True)
print(3>2 or 34<4)
#and
print(not(24>56))
print(not(24>56 or 3<5))

# membership operator
# in , not in 
string1 = "apple is good 4 heat"
print("is" in string1)#T
print("si" in string1)#f
print("apple  is" in string1)#f
print("heat " in string1)

string2 = "apller is 566"
print("5" in string2)#t
print("5"  not in string2)#f


#identity operator
# is , is not
# is operator gives true when we test for same object.
# otherwise False.

# variables data type in python 
# variable/ refrences :

#variable is a refrenes to a memori location where over object beside
num = 90
num2 = 100
num3 = 90
print(id(num))
print(id(num2))
print(id(num3))
# 