import re
import pandas as pd
import csv
from tika import parser
p=[]
#Creating Data Frames
df= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MainGroup1.csv")#importing maingroup xls
df2= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MainSubGroup1.csv")#importing subgroup xls
df5= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\TestList1 - Copy.csv")#importing testlist xls
maingroup=list(df['desc'])
df3=pd.merge(df, df2, right_on='group',left_on='gcode') #merging  maingroup and subgroup
df4=pd.merge(df3, df5, right_on='subgroup',left_on='Tgrpcod')#merging above dataset with testlist
df4=df4[['desc','Desc_x','Desc_y','Result']]

#Main Function
def func(text):
    p=[]
#case where all maingroup ,subgroup and testname matches with the data dictionary
    for l in maingroup:
        pattern=re.compile(l,re.IGNORECASE) #searching maingroup names
        matches=pattern.search(text)
        if(matches):
            b=df['gcode'][df['desc']==l]
            grp=(list(b)[0])
            group=list(df4['Desc_x'][df4['desc']==l])
            group= list(set(group))
            for i in group:
                b=df2['Tgrpcod'][df2['Desc']==i]
                subgrp=(list(b)[0])
                i=i.replace('(','\(',5)
                i=i.replace(')','\)',5)
                i=i.replace('/','\/',5)
                pattern=re.compile(i,re.IGNORECASE) #searching subgroup names
                matches=pattern.search(text)
                if(matches):
                    subgroup=list(df4['Desc_y'][df4['Desc_x']==i])
                    subgroup=list(set(subgroup))
                    for j in subgroup:
                        result=''
                        rang=''
                        if(type(j)==float):
                            continue
                        if(j=='.'):
                            continue

                        try:
                            j=j.replace('(','\(',5) #adding backslash to brackets to make it parsable
                            j=j.replace(')','\)',5)
                            pattern=re.compile(r'^'+j+'\s.*',re.IGNORECASE+re.M)#searching test names
                            matches=pattern.search(text)
                            if(matches):
                                j=j.replace('\(','(',5)
                                j=j.replace('\)',')',5)
                                test=j
                                e,y=matches.span()
                                try:
                                    t=text[e:y].split(j)[1].split(' ')
                                    if(len(t)==2):
                                        if(':' in t[1]):
                                            result=t[2]
                                        else:
                                            result=t[1]
                                        rang=''
                                    elif(len(t)==3):
                                        if(':' in t[1]):
                                            result=t[2]
                                        else:
                                            result=t[1]
                                        rang=t[2]
                                    elif(len(t)>3):
                                        if(':' in t[1]):
                                            result=t[3]
                                        else:
                                            result=t[1]
                                        if(t[-2]=='-'):
                                            rang=t[-3:]
                                            rang=''.join(rang)
                                        else:
                                            rang=t[-1]
                                        if("(" in result):
                                            continue
                                    row=[grp,subgrp,test,result,rang,'Perfect Match']
                                    p.append(row)
                                except:
                                    continue
                        except:
                            pass
#case where maingroup does not match with the data dictionary
    for l in maingroup:
        pattern=re.compile(l,re.IGNORECASE)# searching for maingroup names
        matches=pattern.search(text)
        if(matches):
            break #leaving the loop is maingroup is found
        else:
            group=list(df4['Desc_x'])
            group= list(set(group))
            for i in group:
                i=i.replace('(','\(',5)
                i=i.replace(')','\)',5)
                pattern=re.compile(r'^'+i+'\s.*',re.IGNORECASE+re.M)#searching for subgroup names
                matches=pattern.search(text)
            if(matches):#
                subgroup=list(df4['Desc_y'][df4['Desc_x']==i])
                subgroup=list(set(subgroup))
            else:
                subgroup=list(df4['Desc_y'])
                subgroup=list(set(subgroup))
            for j in subgroup:
                result=''
                rang=''
                if(type(j)==float):
                    continue
                if(j=='.'):
                    continue

                try:
                    j=j.replace('(','\(',5)
                    j=j.replace(')','\)',5)
                    pattern=re.compile(r'^'+j+'\s.*',re.IGNORECASE+re.M)#searching for test names
                    matches=pattern.search(text)
                    if(matches):
                        j=j.replace('\(','(',5)
                        j=j.replace('\)',')',5)
                        i=i.replace('/','\/',5)
                        test=j
                        e,y=matches.span()
                        try:
                            t=text[e:y].split(j)[1].split(' ')
                            if(len(t)==2):
                                if(':' in t[1]):
                                    result=t[2]
                                else:
                                    result=t[1]
                                rang=''
                            elif(len(t)==3):
                                if(':' in t[1]):
                                    result=t[2]
                                else:
                                    result=t[1]
                                rang=t[2]
                            elif(len(t)>3):
                                if(':' in t[1]):
                                    result=t[2]
                                else:
                                    result=t[1]
                                if(t[-2]=='-'):
                                    rang=t[-3:]
                                    rang=''.join(rang)
                                else:
                                    rang=t[-1]
                            b=df5[['subgroup','group']][df5['Desc']==test]
                            sub=(list(b['subgroup'])[0])
                            grp=(list(b['group'])[0])
                            row=[grp,sub,test,result,rang,'Perfect Match']
                            if("(" in result):
                                continue
                            p.append(row)
                        except:
                            continue
                except:
                    pass

#case where subgroup does not match with the data dictionary
    for l in maingroup:
        pattern=re.compile(l,re.IGNORECASE)#searching for groups
        matches=pattern.search(text)
        if(matches):
            group=list(df4['Desc_x'])
            group= list(set(group))
            for i in group:
                i=i.replace('(','\(',5)
                i=i.replace(')','\)',5)
                pattern=re.compile(r'^'+i+'\s.*',re.IGNORECASE+re.M)#searching for subgroups
                matches=pattern.search(text)
            if(matches):
                break
            else:
                subgroup=list(df4['Desc_y'])
                subgroup=list(set(subgroup))
            for j in subgroup:
                result=''
                rang=''
                if(type(j)==float):
                    continue
                if(j=='.'):
                    continue

                try:
                    j=j.replace('(','\(',5)
                    j=j.replace(')','\)',5)
                    pattern=re.compile(r'^'+j+'\s.*',re.IGNORECASE+re.M)#searching for test names
                    matches=pattern.search(text)
                    if(matches):

                        j=j.replace('\(','(',5)
                        j=j.replace('\)',')',5)
                        i=i.replace('/','\/',5)
                        test=j
                        e,y=matches.span()
                        try:
                            t=text[e:y].split(j)[1].split(' ')
                            if(len(t)==2):
                                if(':' in t[1]):
                                    result=t[2]
                                else:
                                    result=t[1]
                                rang=''
                            elif(len(t)==3):
                                if(':' in t[1]):
                                    result=t[2]
                                else:
                                    result=t[1]
                                rang=t[2]
                            elif(len(t)>3):
                                if(':' in t[1]):
                                    result=t[3]
                                else:
                                    result=t[1]
                                if(t[-2]=='-'):
                                    rang=t[-3:]
                                    rang=''.join(rang)
                                else:
                                    rang=t[-1]
                            b=df5[['subgroup','group']][df5['Desc']==test]
                            sub=(list(b['subgroup'])[0])
                            grp=(list(b['group'])[0])
                            row=[grp,sub,test,result,rang,'Perfect Match']
                            if("(" in result):
                                continue
                            p.append(row) #adding rows to p
                        except:
                            continue
                except:
                    pass

    return p
