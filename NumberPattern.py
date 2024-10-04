rows =int(input("Enter the number of the Rows requried: "))

print(f'The right angle pattern\n')
for row in range(1,rows+1):
    for cols in range(row):
        print(chr(cols + 49), end=" ")
    print()

print()

print(f'The inverse right angle pattern:\n')
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(chr(cols + 49), end=" ")
    print()
print()
print(f'The Triangle pattern:')   
for row in range(rows+1):
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(chr(cols + 49), end=" ")
    for cols in range(row-1):
        print(chr(cols + 49), end =" ")
    print()

print()
print(f'The inverse triangle pattern:\n')
for row in range(rows):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(chr(cols + 49), end=" ")
    for cols in range(rows-row-1):
        print(chr(cols + 49), end=" ")
    print()

print()
print(f'The Diamond pattern:') 

for row in range(rows):
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(chr(cols + 49), end=" ")
    for cols in range(row-1):
        print(chr(cols + 49), end=" ")
    print()  
for row in range(rows):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(chr(cols + 49), end=" ")
    for cols in range(rows-row-1):
        print(chr(cols + 49), end=" ")
    print()

print()
print(f'The star pattern\n')
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(chr(cols + 49), end=" ")
    for cols in range(row+1):
        print(chr(cols + 49), end=" ")    
    print()
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(chr(cols + 49), end=" ")
    for cols in range(rows):
        print(chr(cols + 49), end=" ")
    for cols in range(rows):
        print(chr(cols + 49), end=" ")
    for cols in range(rows-row+1):
        print(chr(cols + 49), end=" ")
    print()
for row in range(row):
    for cols in range(rows-row-1):
        print(" ", end=" ")
    for cols in range(row+1):
        print(chr(cols + 49), end=" ")
    for cols in range(rows):
        print(chr(cols + 49), end=" ")
    for cols in range(rows):
        print(chr(cols + 49), end=" ")
    for cols in range(row+2):
        print(chr(cols + 49), end=" ")
    print()
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(chr(cols + 49), end=" ")
    for cols in range(rows-row+1):
        print(chr(cols + 49), end=" ") 
    print()