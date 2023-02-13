total=0#initialise total
count=0#initialise count
max_v=0#initialise max value
min_v=None#initialise min value
while True:
    prompt='Please enter the sales number:'
    u_sales_n=input(prompt)
    if u_sales_n=='done': #break the while loop if done command by operator
        break
    else:
        try:
            sales_n=int(u_sales_n)#check if a number is entered
            print('Your entry is accepted!')
            total=total+sales_n#update the total
            count=count+1#update the count
            average=total/count#calculate the average
            if sales_n>max_v:
                max_v=sales_n#update the maximum value
            if min_v==None:
                min_v=sales_n#update the minimum value for the very first loop execution
            elif sales_n<min_v:
                min_v=sales_n#update the min value after the first loop execution  
        except:
            print('Please enter a number!')#error message if words are entered

print('Total sales value is', total)
print('Sales count is', count)
print('Average sales value is', average)  
print('Minimum sales value is', min_v)
print('Maximum sales value is', max_v)

    
