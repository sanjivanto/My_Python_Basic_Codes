prompt1="Please enter the projected interest rate:"
prompt2="Please enter the projected growth level:"
prompt3="Please enter the most recent divident:"
prompt4="Please enter the number of shares:"


#function definition to detect interest rate
def get_interest_rate(i_rate):
    if i_rate=='high':
        i_rate=20.0#High interest rate is projected to be 20.0%
        return i_rate
    elif i_rate=='medium':
        i_rate=10.0#Medium interest rate is projected to be 10.0%
        return i_rate
    elif i_rate=='low':
        i_rate=8.0#Low interest rate is projected to be 8.0%
        return i_rate


#function definition to detect growth rate
def get_growth_rate(g_rate):
    if g_rate=='high':
        g_rate=7.5#High growth rate is projected to be 7.5%
        return g_rate
    elif g_rate=='medium':
        g_rate=5.0#Medium growth rate is projected to be 5.0%
        return g_rate
    elif g_rate=='low':
        g_rate=2.5#Low growth rate is projected to be 2.5%
        return g_rate


#get interest rate selection from user and find the projected interest rate
u_i_rate=input(prompt1)
i_rate=u_i_rate.lower()#operator entry is accepted irrespective of the letter case
if i_rate!='high' and i_rate!='medium' and i_rate!='low':
    print('Please enter either High, Medium or Low as interest rate')
else: 
    print('Your entry is accepted!')


#get growth rate selection from user and find the projected growth rate
u_g_rate=input(prompt2)
g_rate=u_g_rate.lower()#operator entry is accepted irrespective of the letter case
if g_rate!='high' and g_rate!='medium' and g_rate!='low':
    print('Please enter either High, Medium or Low as growth rate')
else:
    print('Your entry is accepted!')


#get divident from user
divident_l=input(prompt3)
try:
        divident=int(divident_l)#divident must be a numeric value
        if divident>=0 and divident<100 :#divident must be a positive value
            print('Your entry is accepted')
        else:#divident must be a positive value 
            print('Please enter a value between zero and hundred')    
except:
        print('Enter a number as divident')


#get number of shares from user
shares_l=input(prompt4)
try:
    shares=int(shares_l)#number of shares must be a numeric value
    if shares>=0:#number of shares must be a positive value
        print('Your entry is accepted')
    else:
        print('Please enter a value greater than zero')
except:
        print('Enter a number as number of shares')    

#calculation
stock_price= divident/(get_interest_rate(i_rate)-get_growth_rate(g_rate))#P=D/(R-G)
market_value=stock_price*shares#MV=P*S

#return
print('Projected market value of your investment is $', market_value)

