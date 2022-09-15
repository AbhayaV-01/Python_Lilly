from ast import pattern
import re
set=('ABC,123,234,4444,2345,222,03-May-2022')

#single search
# pattern= re.compile(r'\d\d\d')
# matches=pattern.search(set)
# print(matches)

# pattern= re.compile(r'\d\d\d')
# matches=pattern.finditer(set)
# for match in matches:
#     #print(match)
#     #print("\nmatch.group\n")
#     print(match.group())

# print(type(matches))

# pattern= re.compile(r'\d{3,5}')
# matches=pattern.finditer(set)
# for match in matches:
#     #print(match)
#     #print("\nmatch.group\n")
#     print(match.group())

# print(type(matches))

# datepattern= re.compile(r'\d\d\-[A-Za-z]{3}\-\d\d\d\d')
# matches=datepattern.finditer(set)
# for match in matches:
#     #print(match)
#     #print("\nmatch.group\n")
#     print(match.group())

text = """ Hi, today is 14-Apr-2021, yesterday was 13-Apr-2021 and tomorrow will be 15-Apr-2021.
My schedule is free on 26-04-2021, 06.05.21 and 16/Jun/2021.
You can reach out to me at abnavemangesh@local.com or local_1@local.com & support@local.co.in
you can also call me at one of the following no's +603-007 1212, +6099.100 3344, 017-99988800. """

pattern = re.compile(r'[A-Za-z0-9_]*@[A-Za-z0-9\.]*')
matches = pattern.finditer(text)
for match in matches:
    print(match.group())

pat1= re.compile(r'[\+]{0,1}\d{3,4}[-.][0-9 ]+')
m=pat1.finditer(text)
for match in m:
    print(match.group())
    f=open('reg.txt','a')
    f.write(match.group())
f.close()