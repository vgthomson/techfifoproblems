num = [22,55,34,98,3,1,42,1029]
size = len(num)
for i in range(size):
    maximum_value = i
    for j in range(i+1):
        if num[j]<num[maximum_value]:
            maximum_value = j
        num[i],num[maximum_value]=num[maximum_value],num[i]
print(num)

person = {'a':[1,2,3],'b': 1,'c':5,'d':[10,20]}
sum=0
for i in person.values():
    if type(i) == int:
        sum = sum+i

    if type(i) == list:
        for j in len(i):
            sum=sum+j
print(sum)