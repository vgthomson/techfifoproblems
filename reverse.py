#Problem 17: Write a program reverse.py to print lines of a file in reverse order.
file1 = open('she.txt','w')
sentence = '''She sells seashells on the seashore;The shells that she sells are seashells I'm sure.So if she sells seashells on the seashore,I'm sure that the shells are seashore shells'''
file1.write(sentence)
file1.close()
file1 = open('she.txt','r')
reading=file1.readlines()
print(reading[::-1])
file1.close()
