feedback=input('Please give your feedback!\n')
bad=feedback.count('bad')#use string.count to count the word bad
unhappy=feedback.find('unhappy')#use string.find to find the presence of word unhappy
upset=feedback.find('upset')#use string.find to find the presence of word upset
if bad>0 or unhappy>=0 or upset>=0:#if count>0 or if position is greater than -1 negative word is present
    print('Negative sentiment')
a=[1,2,3]
print(max(a))