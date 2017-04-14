import re
# import name list
with open('/gazetteer/person_female.lst') as f:
    female = f.read().splitlines()
with open('/gazetteer/person_male.lst') as f:
    male = f.read().splitlines()

namelist = female + male

def MaskName(text):
    Name = []
    for one in namelist:
        text_split = text.split()
        for word in text_split:
            if word == one:
                Name.append(word)
    for item in Name:
        text = re.sub(item, '*****', text)
    return (text)

def MaskEmail(text):
    Email = re.findall('(([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})+)',text)
    for item in Email:
        text = re.sub(item[0], '%s*****' %item[0][0], text)
    return (text)

def MaskPhone(text):
    Phone = re.findall('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',text)
    for item in Phone:
        text = re.sub(item, '%s*****' %item[0][0], text)
    return (text)

def MaskPin(text):
    Pin = re.findall('\D(\d{4})\D',text)
    for item in Pin:
        text = re.sub(item, '****', text)
    return (text)

def MaskTwitter(text):
    Twitter = re.findall('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)',text)
    for item in Twitter:
        text = re.sub(item, '*****', text)
    return (text)
