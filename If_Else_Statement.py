#If Else Statements
If_Else_Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))

Python Conditions

Equal						-> x == y
Not Equal					-> x != y
Less than					-> x < y
Less than or equal to 		-> x <= y
Greater than 				-> x > y
Greater than or equal to	-> x >= y
Boolean OR					-> x or y , x | y
Boolean AND					-> x and y, x & y
Boolean NOT 				-> not x

if -
else - 

#IF Statement

x = 70
y = 70

if x > y: 
	print("x is greater than y ")
elif x == y:
	print("x and y are equal")

#Else

x = 50
y = 150

if x > y:
	print("x is greater than y")
else x == y:
	print("x and y are equal")
else:
	print("x is less than y")

#Short Hand If

if x > y: print("x is greater than y")

#Short Hand If ... Else

x = 50
y = 150

print(x) if x > y else print(y)


#And is logical operator

x = 50
y = 40
z = 100

if x > y and z > x:
	print("All Conditions are True")

#Or is logical operator

x = 50
y = 40
z = 100

if x > y or z < y:
	print("one of the conditions is True")
elif x > y and z > y:
	print ("All conditions are True")
else:
	print("nothing else")

#Nested If is if statements in if statements

x = 50

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No,x is not greater than 20")

elif x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")
else: 
	print("x is not greater than 10 & 20")

#-----------#
HomeWork

if siyb student
	if python or unity or ai
		if boy or girl
		else
	else
else:

x = input(str("Are you SIYB student : "))

y = input(str("Are you Python student : "))

z = input(str("Boy or Girl : "))

if x == "siyb":
	print("Yes I'm SIYB student")
	if y == "python":
			print("Yes, I'm Python student")
			if z == "boy" or z = "girl":
				print("gender")
	else: 
		print("not")
