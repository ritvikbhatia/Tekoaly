import csv
from tika import parser
import namedetails
import testdetails
import remaining
import os
import logging
count=0
logging.basicConfig(filename='app.log',level=logging.INFO) #to create a log file
ori="C:\\Users\\Ritvik\\Desktop\\Tekoaly\\PDF "#folder where you put the PDFS
os.chdir(ori) #changing the directory
dirs=os.listdir() #getting list of directories
#adding column names to test results.csv
with open('C:\\Users\\Ritvik\\Desktop\\tekoaly\\'+'Test Results'+'.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Group ID','Subgroup ID','Test Name','Result','Standard Range','Match Type','Patient ID'])
#adding column names to name details.csv
with open('C:\\Users\\Ritvik\\Desktop\\tekoaly\\'+'Patient Details'+'.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Patient ID','Date','Name','Mobile no','referred By','Age','Company','Gender'])


for file  in dirs: # iterating in the folder

#Generating patient ID
    id='C0'
    id=id+str(count)
    count=count+1

#converting PDF to text
    try:
        file_data = parser.from_file(file)
        text = file_data['content']
    except:
        print("File not available")
        continue
#For Patient details
    row=[id,namedetails.date(text),namedetails.name(text),namedetails.mob(text),namedetails.ref(text),namedetails.srl(text),namedetails.age(text),namedetails.comp(text),namedetails.sex(text)]
    with open('C:\\Users\\Ritvik\\Desktop\\tekoaly\\'+'Patient Details'+'.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
#For Test Details
    p=[]
    p=testdetails.func(text) #calling a fuction to get test details
    p=list(set(map(tuple,p))) #removing duplicates
    p=[list(p) for p in set(tuple(element) for element in p)] #typecasting to a list
    with open('C:\\Users\\Ritvik\\Desktop\\tekoaly\\'+'Test Results'+'.csv', 'a') as csvFile:
        for i in range(len(p)):
            writer = csv.writer(csvFile)
            writer.writerow(p[i]+[id])
#For remaining testnames
    ls=[]
    ls=remaining.relevence(text) #calling a fuction to get remaining details
    with open('C:\\Users\\Ritvik\\Desktop\\tekoaly\\'+'Test Results'+'.csv', 'a') as csvFile:
        for i in range(len(ls)):
            writer = csv.writer(csvFile)
            writer.writerow(ls[i]+[id])
