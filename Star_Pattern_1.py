rows =int(input("Enter the number of the Rows requried: "))
symbol = input("Enter the character you want to print in Patterns: ")

print(f'The "{symbol}" in right angle pattern\n')
for row in range(1,rows+1):
    for cols in range(row):
        print(symbol, end=" ")
    print()

print()

print(f'The "{symbol}" in inverse right angle pattern:\n')
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(symbol, end=" ")
    print()
print()
print(f'The "{symbol}" in Triangle pattern:')   
for row in range(rows+1):
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(symbol, end=" ")
    for cols in range(row-1):
        print(symbol, end =" ")
    print()

print()
print(f'The "{symbol}" in inverse triangle pattern:\n')
for row in range(rows):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(symbol, end=" ")
    for cols in range(rows-row-1):
        print(symbol, end=" ")
    print()

print()
print(f'The "{symbol}" in Diamond pattern:') 

for row in range(rows):
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(symbol, end=" ")
    for cols in range(row-1):
        print(symbol, end=" ")
    print()  
for row in range(rows):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(symbol, end=" ")
    for cols in range(rows-row-1):
        print(symbol, end=" ")
    print()
print()
print(f'The "{symbol}" in star pattern\n')
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(symbol, end=" ")
    for cols in range(row+1):
        print(symbol, end=" ")    
    print()
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(symbol, end=" ")
    for cols in range(rows):
        print(symbol, end=" ")
    for cols in range(rows):
        print(symbol, end=" ")
    for cols in range(rows-row+1):
        print(symbol, end=" ")
    print()
for row in range(row):
    for cols in range(rows-row-1):
        print(" ", end=" ")
    for cols in range(row+1):
        print(symbol, end=" ")
    for cols in range(rows):
        print(symbol, end=" ")
    for cols in range(rows):
        print(symbol, end=" ")
    for cols in range(row+2):
        print(symbol, end=" ")
    print()
for row in range(rows+1):
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(" ", end=" ")
    for cols in range(row):
        print(" ", end=" ")
    for cols in range(rows-row):
        print(symbol, end=" ")
    for cols in range(rows-row+1):
        print(symbol, end=" ") 
    print()
