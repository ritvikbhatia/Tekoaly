import pandas as pd
import csv
from tika import parser
import namedetails
import testdetails
import os
import logging
count=0
logging.basicConfig(filename='app.log',level=logging.INFO)
file="C:\\Users\\Ritvik\\Desktop\\Tekoaly\\PDF\\24.pdf "

id='C0'
id=id+str(count)
count=count+1
file_data = parser.from_file(file)
text = file_data['content']

p=testdetails.func(text)
p=list(set(map(tuple,p)))

p=[list(p) for p in set(tuple(element) for element in p)]
for i in range(len(p)):
    print(p[i])



# row=[id,namedetails.date(text),namedetails.name(text),namedetails.ref(text),namedetails.srl(text),namedetails.age(text)+namedetails.agesex(text),namedetails.comp(text),namedetails.sex(text)+namedetails.sexage(text)]
# print(row)
