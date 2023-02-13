list1=[]
list2=[]
while True:
    input1=input('enter the list-1 items:')
    if input1=='done':
        break
    else:
        list1.append(input1)
        continue
while True:
    input2=input('enter the list-2 items:')
    if input2=='done':
        break
    else:
        list2.append(input2)
        continue
print('list-1:',list1)
print('list-2:',list2)
for i in list2:
    if i in list1:
        list1.remove(i)
print('Modified list-1:',list1)
