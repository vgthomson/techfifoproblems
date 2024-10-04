'''
#Problem 17: Write a program reverse.py to print lines of a file in reverse order.
openfile = open('she.txt', "r")
result = list()
for lines in openfile:
    separatelines = lines.splitlines()
    for i in separatelines:
        result.append(i)
for j in result[::-1]:
    print(j)
openfile.close()


#Problem 18: Write a program to print each line of a file in reverse order.
openfile = open('she.txt', "r")
thelist =[]
reversedlist = []
for lines in openfile:
    separatelines = lines.splitlines()
    for i in separatelines:
        thelist.append(i)
for i in thelist:
    reversedlist.append(i[::-1])
for k in reversedlist:
    print(k)
openfile.close()

#Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

def wrap(fil,size):
    if fil:
        try:
            ope = open(fil)
        except FileNotFoundError:
            print("File Not Exist")
    for i in ope:
        print(i[:size],"\n",i[size:]n )
wrap("she.txt",30)
openfile.close()
    


#Problem 23: Write a program center_align.py to center align all lines in the given file.
openfile = open('she.txt', "r")
result = list()
for lines in openfile:
    separatelines = lines.center(100)
    print(separatelines)
openfile.close()    

    '''