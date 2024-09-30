#Problem 1: What will the output of the following program.
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f()) #A B
print(a.g(), b.g()) #A B

#Problem 2: What will be the output of the following program?
try:
    print ("a") #This will print
except:
    print ("b") #This will skipped
else:
    print ("c") #This will print
finally:
    print ("d") #This will print

#Problem 3: What will be the output of the following program?
try:
    print("a") #This will print
    raise Exception("doom")
except:
    print("b") #This will print
else:
    print("c") #Will skip because try raised an error.
finally:
    print("d") #This will print

#Problem 4: What will be the output of the following program?
def f():
    try:
        print("a") #This will print
        return
    except:
        print("b") #Try block is executed without exception
    else:
        print("c") #try has return keyword hence else is not printed
    finally:
        print("d") #Finally always prints even if a exit statement is there(break,continue,return)
f()