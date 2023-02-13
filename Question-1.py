d={}
text=input('Enter the text\n')
text=text.lower()#count irrespective of the letter case
text=text.replace(' ','')#remove the white spaces
for letter in text:
    d[letter]=d.get(letter,0)+1# get method to append new items or add existing item count
print(d)
