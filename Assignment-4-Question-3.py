list1=[]
while True:
    try:
        input1=int(input('enter the lower bound index:'))
        print('Entry accepted!')     
        break
    except:
        print('Enter a number')   
        continue 
while True:
    try:
        input2=int(input('enter the upper bound index:'))
        if input2>input1:
            print('Entry accepted!')
            break  
        else:
            print('Upper bound index should be greater than lower bound index')     
            continue
    except:
        print('Enter a number')   
        continue 
while True:
    input3=input('Enter number for list:')
    if input3=='done':
        break
    try:
        input3=int(input3)
        print('Entry accepted!')
        list1.append(input3)
    except:
        print('Enter a number')   
        continue   
print('list:',list1[input1:input2])
print('Length:',len(list1[input1:input2]))
print('Maximum:',max(list1[input1:input2]))
print('Minimum:',min(list1[input1:input2]))
print('Sum:',sum(list1[input1:input2]))


