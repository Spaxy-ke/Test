first_name="Jack"
second_name="Sparrow"
age=20
height=150.25
male=True
female=False
print ("Hello World I am"+first_name+" "+second_name+" and my age is "+str(age))
print("Used data types are")
print(type(first_name))
print(type(age))
print(type(height))
print(type(male))
age=age+1
height=height+12
print("After 1 year i will be "+str(age)+ " with a height of "+str(height ))
print("are you male:"+str(male))
print("are you female: "+ str(female)) 
# Multiple assignment
name,marks,height="brian",30,256.23
print(name*3)
print( marks)
print( height)
# String methods
eg = "I am a Hacker"
print(len(eg))
print(eg.isspace())
print(eg.swapcase())
# Type Casting
print("My age in float numbers is "+str(float(age))+"my height in int is "+str(int(height)))
