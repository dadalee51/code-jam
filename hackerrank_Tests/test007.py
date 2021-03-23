import csv
from collections import namedtuple as nt
a=nt('MenuItem','food,price,temp')
cr=csv.reader(open('test.csv'))
menu=[]
for i in cr:
    menu.append(a._make(i))
#so namedtuples are used to make accessing fields a lot easier by creating a type.