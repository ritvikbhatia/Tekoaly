from fuzzywuzzy import process
from tika import parser
import dictionaryy
import testdetails
import re
import pandas as pd
def relevence(text):
    ls=[]
    df= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MainGroup1.csv")#importing maingroup xls
    df2= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\MainSubGroup1.csv")
    df5= pd.read_csv("C:\\Users\\Ritvik\\Desktop\\Tekoaly\\TestList1 - Copy.csv")
    df3=pd.merge(df, df2, right_on='group',left_on='gcode') #merging  maingroup and subgroup
    df4=pd.merge(df3, df5, right_on='subgroup',left_on='Tgrpcod')

    # file ='C:\\Users\\Ritvik\\Desktop\\Tekoaly\\PDF\\24.pdf'
    # file_data = parser.from_file(file)
    # text = file_data['content']


    #removing testnames
    p=testdetails.func(text)
    for i in range(len(p)):
        p[i][2]=p[i][2].replace('(','\(',5)
        p[i][2]=p[i][2].replace(')','\)',5)
        pattern=re.compile(p[i][2]+'.+',re.IGNORECASE)
        matches=pattern.search(text)
        if(matches):
            e,y=matches.span()
            text=text.replace(text[e:y],'',10)

    #removing Juck
    p=dictionaryy.retdic()
    for i in range(len(p)):
        pattern=re.compile(p[i]+'.+',re.IGNORECASE+re.M)
        matches=pattern.findall(text)
        for j in matches:
            # e,y=matches.span()
            text=text.replace(j,'',10)

    #removing subgroups
    subgrp=list(df2.Desc)
    for i in range(len(subgrp)):
        text=text.replace(subgrp[i],'',10)

    #removing group names
    grp=list(df.desc)
    for i in range(len(grp)):
        text=text.replace(grp[i],'',10)

    choices=list(df5.Desc)
    # print(text)
    pattern=re.compile('^[a-z]+[\s/-]+.+',re.IGNORECASE+re.M)
    matches=pattern.findall(text)
    # print(matches)
    for i in range(len(matches)):
        row=[]
        match=matches[i].split(' ')
        if(len(match)==1):
            continue
        if(match[-2]=='-'):
            match[0]=' '.join(match[0:-5])
            test,score=process.extractOne(match[0], choices)
            match=match[-5:]
            result=match[0]
            rang=match[-3:]
            rang=''.join(rang)
            b=df5[['subgroup','group']][df5['Desc']==test]
            sub=(list(b['subgroup'])[0])
            grp=(list(b['group'])[0])
            row=[grp,sub,test,result,rang,'Fuzzy Match']
            ls.append(row)
        elif(len(match)>3):
            match[0]=' '.join(match[0:-3])
            # print(match[0])
            test,score=process.extractOne(match[0], choices)
            if(score>90):
                test,score=process.extractOne(match[0], choices)
                match=match[-3:]
                result=match[0]
                rang=match[-1]
                b=df5[['subgroup','group']][df5['Desc']==test]
                sub=(list(b['subgroup'])[0])
                grp=(list(b['group'])[0])
                row=[grp,sub,test,result,rang,'Fuzzy Match']
                ls.append(row)
        else:
            val,score=process.extractOne(match[0], choices)
            if(score>90):
                # print(match)
                rang=match[-1]
                result=match[1]
                b=df5[['subgroup','group']][df5['Desc']==val]
                sub=(list(b['subgroup'])[0])
                grp=(list(b['group'])[0])
                row=[grp,sub,val,result,rang,'Fuzzy Match']
                ls.append(row)


    return(ls)
