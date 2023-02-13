d={}
numbers=[]
squre_l=[]
while True:
    inp=input('enter sequence of numbers:')#user inputs
    if inp=='done' or inp=='stop':#enter stop command
        break
    try:
        inp=int(inp)
        print('Entry accepted!')
        numbers.append(inp)     
    except:
        print('Enter a number')   
        continue
for number in numbers:
    squre_l.append(number**2)
new_l=numbers+squre_l#new list with square of input values
for x in new_l:
    if new_l.index(x)%2==0:#find the index and if index is even (0,2,4 etc.) append to dictionary
        d[new_l.index(x)]=x
    else:
        continue
print(d)

