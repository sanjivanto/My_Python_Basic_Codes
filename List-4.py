list1=[]
zero=0
negative_even=0
negative_odd=0
positive_even=0
positive_odd=0
while True:
    input1=input('Enter number for list:')
    if input1=='done':
        break
    try:
        input1=int(input1)
        print('Entry accepted!')
        list1.append(input1)
    except:
        print('Enter a number')   
        continue   
for digit in list1:
    if digit==0:#check for zero
        zero=zero+1
    if digit>0 and digit%2==0: #check for positive even numbers
        positive_even=positive_even+1
    if digit>0 and digit%2!=0: #check for positive odd numbers
        positive_odd=positive_odd+1
    if digit<0 and digit%2==0:#check for negative even numbers
        negative_even=negative_even+1
    if digit<0 and digit%2!=0: #check for negative odd numbers
        negative_odd=negative_odd+1
print('list:',list1)
print('Number of positive odd numbers:', positive_odd)
print('Number of negative odd numbers:', negative_odd)
print('Number of positive even numbers:', positive_even)
print('Number of negative even numbers:', negative_even)
print('Number of zeroes:', zero)





