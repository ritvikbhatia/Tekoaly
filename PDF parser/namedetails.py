import re
import logging
logging.basicConfig(filename='app.log',level=logging.DEBUG)


#For Name
def name(text):
    pattern=re.compile(r'Name[:\s]+[/:a-z.]+\s[a-z.]+\s+[a-z.]+',re.IGNORECASE)
    matches=pattern.search(text)
    e,y=matches.span()
    name=text[e:y].split(' ')
    name=name[1:]
    if(name[2]=='age' or name[2]=='Age' or '\n' in name[2] ):
        name=name[0:2]
    elif(name[1]=='age' or name[1]=='Age' ):
        name=name[0:1]
    elif(name[-1]=='age' or name[-1]=='Age'or '\n'in name[-1]) :
        name=name[0:-1]
    if(name[0]==':'):
        name=name[1:]

    name=' '.join(name)
    return(name)

# for date
def date(text):
    pattern=re.compile(r'date[:\s]+[:0-9]+[/-][\da-z]+[/-]\d+',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        date=text[e:y].split(' ')[1]
    except:
        date=''
    return(date)


#for age
def age(text):
    pattern=re.compile(r'age[:\s]+\d+',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        age=text[e:y].split(' ')[1]
    except:
        age=''
    return(age)

#for sex
def sex(text):
    pattern=re.compile(r'sex[:\s]+[mf]',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        sex=text[e:y].split(' ')[1]
    except:
        sex=''
    return(sex)

def agesex(text):
    pattern=re.compile(r'Age/Gender.+',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        sex=text[e:y].split(' ')[-2]
    except:
        sex=''
    return(sex)

def sexage(text):
    pattern=re.compile(r'Age/Gender.+',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        sex=text[e:y].split('/')[-1]
        if(sex=='Female'):
            sex='F'
        elif(sex=='Male'):
            sex='M'
    except:
        sex=''
    return(sex)

#for srlno
def srl(text):
    pattern=re.compile(r'srl no.[:\s]+\d+',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        srl=text[e:y].split(' ')[2]
    except:
        srl=''
    return(srl)

#for ref
def ref(text):
    pattern=re.compile('(Ref. by[:\s]+.+)|(Referred by[:\s]+.+)',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        ref=text[e:y].split(' ')[2:]
        if(ref[0]=='Company'):
            ref=''
        if('Company'in ref[-1]) :
            ref=ref[0:-1]
        ref=' '.join(ref)

    except:
        ref=''
    return(ref)


#for company
def comp(text):
    try:
        pattern=re.compile('(company[:\s]+[a-z]+)|(Sample from[:\s]+[a-z]+)',re.IGNORECASE)
        matches=pattern.search(text)
        e,y=matches.span()
        try:
            comp=text[e:y].split(' ')[-1]
            if('\n' in comp):
                comp=comp.split('\n')[-1]
        except:
            comp=''
    except:
        comp=''
    return(comp)

def mob(text):
    pattern=re.compile(r'mobile no.[:\s]+\d+',re.IGNORECASE)
    matches=pattern.search(text)
    try:
        e,y=matches.span()
        age=text[e:y].split(' ')[2]
    except:
        age=''
    return(age)
