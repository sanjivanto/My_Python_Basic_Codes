numbers=[]
count=0
while True:
    try:
        input1=int(input('Enter the number to check:'))
        print('Entry accepted!')     
        break
    except:
        print('Enter a number')   
        continue 
while True:
    input2=input('Enter number for list:')
    if input2=='done' or input2=='stop':
        break
    try:
        input2=int(input2)
        print('Entry accepted!')
        numbers.append(input2)
    except:
        print('Enter a number')   
        continue 
for number in numbers:
    if number==input1:
        count=count+1
print(numbers)
print('count:',count)
