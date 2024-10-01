
#Problem 1:
x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x) 
x[2] = 2 
print(x)

"""Output:
[0, 1, [3]]
[0, 1, [3, 4]]
[0, 1, 2]"""



#Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.
#sum(["hello", "world"])
#sum(["aa", "bb", "cc"])

ab = "".join(["hello", "world"]) #We cannot modify sum function since it is deals with intergers
print(ab)


#Problem 4: Implement a function product, to compute product of a list of numbers.


def product(a):
    global x
    x = 1
    for i in a:
        x = x*i
    return x
print(product([1, 2, 3]))

#Problem 5: Write a function factorial to compute factorial of a number. 
# Can you use the product function defined in the previous example to compute factorial?
def factorial(z):
    if z == 0 or z==1:
        print(1)
    else:
        values = range(1,z+1)
        return product(values)
print(factorial(4))

#Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?

ages = [22,65,34,33] 
print(ages[::-1]) #Reversing the list using slicing
ages.reverse() 
print(ages) #Reversing the list using reverse function

#Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. 
#Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?

print(min(ages)) #Prints minimum age
print(max(ages)) #Prints maximum age
name = ['ashok', 'arun', 'gokul']
print(min(name)) #lexicographically largest name
print(max(name)) #lexicographically largest name

#Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
#Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?
def cumulative_sum(listofnumbers):
    global y
    y = 0
    result = []
    for i in listofnumbers:
        y = y+i
        result.append(y)
        i = y
    return result
print(cumulative_sum([1, 2, 3, 4])) #Return cumulative sum of the list

#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.
def cumulative_product(listofnumbers):
    global x
    x = 1
    result = []
    for i in listofnumbers:
        x = x*i
        result.append(x)
        i = y
    return result

print(cumulative_product([4, 3, 2, 1])) #Return cumulative product of the list

#Problem 10: Write a function unique to find all the unique elements of a list.
def unique(values):
    unique_values =set()
    for i in values:
        unique_values.add(i)
    return print(list(unique_values))

unique([1, 2, 1, 3, 2, 5])

#Problem 11: Write a function dups to find all duplicates in the list.
def dups(values):
    unique_values = set(values)
    result =[]
    for i in values:
        if i in unique_values:
            unique_values.remove(i)
        else:
            result.append(i)
    return print(result)
dups([1, 2, 1, 3, 2, 5]) #[1,2]


#Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.
def group(values,size):
    result = []
    for i in range(0,len(values),size):
        result.append(values[i:i+size])
    return print(result)    
        
group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) #Result=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) #Result=[[1, 2, 3, 4], [5, 6, 7, 8], [9]]

#Problem 13: Write a function lensort to sort a list of strings based on length.
def lensort(values):
    values.sort(key=lambda x:len(x))
    return print(values)
    
lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']) #Result=['c', 'perl', 'java', 'ruby', 'python', 'haskell']

#Problem 14:
#Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
def unique(values, key=None):
    result = set()
    distinctvalues = []      
    for i in values:
        if key:
            value = key(i)
        if value not in result:
            result.add(value) 
            distinctvalues.append(i)
    return print(distinctvalues) #['python', 'java']

unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())


#Problem 16: Write a function extsort to sort a list of files based on extension.

def extsort(files):
    files.sort(key=lambda x:[x.split('.')[-1]])
    return print(files)
extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
#['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']

#Problem 24: Provide an implementation for zip function using list comprehensions.
k = [x for x in zip([1, 2, 3], ["a", "b", "c"])]
print(k)

#Problem 25: Python provides a built-in function map that applies a function to each element of a list.
#Provide an implementation for map using list comprehensions.

def square(x): return x * x
result = map(square, range(5))
print(list(result)) #[0, 1, 4, 9, 16]

#Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true.
#Provide an implementation for filter using list comprehensions.

def even(x): return x %2 == 0
result=filter(even, range(10))
print(list(result)) #[0, 2, 4, 6, 8]


#Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n.
#Please note that (a, b, c) and (b, a, c) represent same triplet.
def triplets(n):
    result = [(a,b,c) for a in range(1,n) for b in range(a,n) for c in range(b,n) if a+b==c and b+a == c]
    return print(result)
triplets(5)

#Problem 29: Write a function array to create an 2-dimensional array.
#The function should take both dimensions as arguments. Value of each element can be initialized to None
def array(a,b):
    return [[None for _ in range(b)] for _ in range(a)]
a = array(2, 3)
print(a) #[[None, None, None], [None, None, None]]
a[0][0]=5
for i in a:
    print(i,end=" ") #[[5, None, None], [None, None, None]]


