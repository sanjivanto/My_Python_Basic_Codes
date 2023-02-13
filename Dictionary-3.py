d={}
k1=input('Enter header for column one:')
k2=input('Enter header for column two:')
k3=input('Enter header for column three:')

fn=input('Enter first names:')#enter the first names
fn=fn.split()
while True:
    ln=input('Enter last names:')#enter the last names
    ln=ln.split()
    if len(ln)==len(fn):#if last name count and first name counts not matching, try again
        break
    else:
        print('Number of first names and last names are not same; try again!')
        continue
while True:
    age=input('Enter ages:')#enter the ages
    age=age.split()
    if len(age)==len(ln):#if age count and last name counts not matching, try again
        break
    else:
        print('Number of ages enterd not matching with the number of names enterd; try again!')
        continue
while True:
    height=input('Enter heights:')#enter the heights
    height=height.split()
    if len(height)==len(age):#if height count and age counts not matching, try again
        break
    else:
        print('Number of heights enterd not matching with the number of names enterd; try again!')
        continue
full_name=[]
index=0
for x in fn:
    full_name.append(x+' '+ln[index])#derive the full name
    index=index+1
d[k1]=full_name
d[k2]=age
d[k3]=height
print(d)
