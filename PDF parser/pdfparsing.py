import re
import pandas as pd
import csv
from tika import parser
file ='C:\\Users\\Ritvik\\Desktop\\Tekoaly\\PDF\\21.pdf'
file_data = parser.from_file(file)
text = file_data['content']

# #For Name
# pattern=re.compile(r'Name[\s:]+[:a-z./]+\s[a-z.]+\s+[a-z.]+',re.IGNORECASE)
# matches=pattern.search(text)
#
# e,y=matches.span()
# name=text[e:y].split(' ')
# name=name[1:]
# print(name[-1])
# if(name[2]=='age' or name[2]=='Age'):
#     name=name[0:2]
# elif(name[1]=='age' or name[1]=='Age'):
#     name=name[0:1]
# elif(name[-1]=='age' or name[-1]=='Age'):
#     name=name[0:-1]
# if(name[0]==':'):
#     name=name[1:]
#
# name=' '.join(name)
# print(name)
#
# #for date
# pattern=re.compile(r'date[:\s]+[:0-9]+[/-][\da-z]+[/-]\d+',re.IGNORECASE)
# matches=pattern.search(text)
# e,y=matches.span()
# date=text[e:y].split(' ')[1]
# print(date)
#
# #for age
# pattern=re.compile(r'age[:\s]+',re.IGNORECASE)
# matches=pattern.search(text)
# try:
#     e,y=matches.span()
#     age=text[e:y].split(' ')[1]
# except:
#     age=''
# print(age)
#
# # #for sex
# # pattern=re.compile(r'sex[:\s]+[mf]',re.IGNORECASE)
# # matches=pattern.search(text)
# # e,y=matches.span()
# # sex=text[e:y].split(' ')[1]
# # print(sex)
#
# #for srlno
# # pattern=re.compile(r'srl no.[:\s]+\d+',re.IGNORECASE)
# # matches=pattern.search(text)
# # e,y=matches.span()
# # srl=text[e:y].split(' ')[2]
# # print(srl)
# #
# # #for ref
# pattern=re.compile(r'Ref. by[:\s]+.+',re.IGNORECASE)
# matches=pattern.search(text)
# try:
#     e,y=matches.span()
#     ref=text[e:y].split(' ')[2:]
# except:
#     ref=''
# ref=' '.join(ref)
# if(ref=='Company'):
#     ref=''
# print(ref)
#
# # #for company
# try:
#     pattern=re.compile(r'company[:\s]+[a-z]+',re.IGNORECASE)
#     matches=pattern.search(text)
#     e,y=matches.span()
#     try:
#         comp=text[e:y].split(' ')[-1]
#     except:
#         comp=''
# except:
#     comp=''
# print(comp)

import re
import pandas as pd
import csv
from tika import parser
p=[]
#test details

df= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MainGroup1.csv")
df2= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MainSubGroup1.csv")
df5= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\TestList1 - Copy.csv")
maingroup=list(df['desc'])
df3=pd.merge(df, df2, right_on='group',left_on='gcode')
df4=pd.merge(df3, df5, right_on='subgroup',left_on='Tgrpcod')
df4=df4[['desc','Desc_x','Desc_y','Result']]
df4.drop_duplicates
#df4=df4[df4.Result!='Comments']

for l in maingroup:
    pattern=re.compile(l,re.IGNORECASE)
    matches=pattern.search(text)
    group=list(df4['Desc_x'][df4['desc']==l])
    group= list(set(group))
    if(matches):

        for i in group:
            i=i.replace('(','\(',5)
            i=i.replace(')','\)',5)
            pattern=re.compile(i,re.IGNORECASE)
            matches=pattern.search(text)
            subgroup=list(df4['Desc_y'][df4['Desc_x']==i])
            subgroup=list(set(subgroup))
            testtype=i
            if(matches):
                for j in subgroup:
                    if(type(j)==float):
                        continue
                    if(j=='.'):
                        continue

                    try:
                        j=j.replace('(','\(',5)
                        j=j.replace(')','\)',5)
                        j=j.replace('-','\-',5)

                        pattern=re.compile(j,re.I+re.M)
                        matches=pattern.search(text)
                        if(matches):
                            test=j
                            e,y=matches.span()
                            try:
                                t=text[e:y].split(j)[1].split(' ')
                                if(len(t)==2):
                                    result=t[1]
                                    unit=''
                                    rang=''
                                elif(len(t)==3):
                                    result=t[1]
                                    unit=''
                                    rang=t[2]
                                elif(len(t)>3):
                                    result=t[1]
                                    unit=''
                                    if(t[-2]=='-'):
                                        rang=t[-3:0]
                                        rang=''.join(rang)
                                    else:
                                        rang=t[-1]
                                row=[testtype,test,result,unit,rang]
                                print(row)
                            except:
                                continue
                    except:
                        pass

j='PAPP-A'
j=j.replace('(','\(',5)
j=j.replace(')','\)',5)
j=j.replace('-','\-',5)
pattern=re.compile(j,re.I+re.M)
matches=pattern.search(text)
print(matches)
