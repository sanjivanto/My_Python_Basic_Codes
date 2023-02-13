d={}
while True:
    fn=input('Enter first name or stop the program:')# take the user inputs until user say stop/done
    if fn=='done' or fn=='stop':
        break
    ln=input('Enter last name:')
    pn=input('Enter phone number:')
    name='Full name:'+fn+' '+ln
    d[name]=pn#append the library for each entry
print(d)
