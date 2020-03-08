x = 70
y = 70
z = 50

if x == y:
	print("x is equal to y ")
elif z < y:
    print("z is smaller than y")
elif x > z:
	print("x is greater than equal to y")
else:
    print("nothing")

x = 70
y = 60

print(x) if x > y else print(y)

x = 50
y = 150

print("x is greater than y") if x > y else print("x is less than y")
print("x and y are equal") if x == y else print("x is not equal y")

x = 50
y = 40
z = 100

if x > y and z > x:
    print("All Conditions are True")
elif y > z and z > x:
    print("some conditions are True")
else:
    print("default")

x = int(input("Examination Result :"))

if x < 101 and x >= 90 or x == 100:
    print("Grade A")
elif x <=89 and x >=70:
    print("Grade B")
elif x <= 69 and x >= 60:
    print("Grade C")
elif x <= 59 and x >= 40:
    print("Grade D")
elif x < 39 and x > 0 or x == 0:
    print("Fail")
else :
    print("Wrong Number. Try Again")

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