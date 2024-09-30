
#Problem 2:
#How many multiplications are performed when each of the following lines of code is executed?

#Function which returns the square value.
def square(x):
    return x * x

print(square(5)) #Will return 25(5*5)
print(square(2*5)) #Will return 100 i.e, 2*5=10 is given to function 10*10 (2 times the multiplication is done)

#Problem 3:

x = 1 #Global varialble
def f():
    return x 
print(x) #It returns the value of x which is 1
print(f()) #It returns the value of x which is 1

#Problem 4:

x = 1 #global variable
def f():
    x = 2
    return x 
print(x) #Returns global value of x which is 1
print(f()) #Returns local value of x which is 2
print(x) #Returns global value of x which is 1

#Problem 5:

"""x = 1
def f():
        y = x
        x = 2
        return x + y"""
print(x) #Returns value of x which is 1
print(f()) #Returns error because the variable x is not declared global inside the function
print(x) #Will not execute


#Problem 6:

x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print(x, y) #Returns 2,9 2 is the global x value and 9 is the return value from the function

#Problem 9: What will be output of the following program?

print(2 < 3 and 3 > 1) #True
print(2 < 3 or 3 > 1) #True
print(2 < 3 or not 3 > 1) #True
print(2 < 3 and not 3 > 1) #False


#Problem 10: What will be output of the following program?

x = 4
y = 5
p = x < y or x < z
print(p) #True becasue or required only one true

#Problem 11: What happens when the following code is executed? Will it give any error? Explain the reasons.

x = 2
if x == 2:
    print(x) 
else:
    print(y)
#This function runs fine and prints 2

#Problem 12: What happens the following code is executed? Will it give any error? Explain the reasons.

"""x = 2
if x == 2:
    print(x)
else:
    x +"""
#It will provide error
