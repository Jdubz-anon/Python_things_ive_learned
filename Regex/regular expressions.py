import re

test_string = '123abc456789ABC123abc.'
pattern = re.compile(r'\W')# create the pattern
matches = pattern.finditer(test_string) #use pattern to find mathces
#matches = re.finditer(r'abc',test_string)
#matches = re.findall(r'abc',test_string) #prints out abc as many times as abc is found
####methods for matching pattern: match(),search(),findall()
#match method finds a match in the begining of a string only
#search method finds a match anywhere in the string
#####methods us to modify method split(), sub()
for match in matches:
####methods that can be used on the matches group(),span(),start(),end()
    #print(match.span(), match.start(), match.end())
    print(match.group())
############################################################
#SETS
import re
test_string = 'hello123_ heyho hohey'
pattern = re.compile(r'[a-zA-Z0-9]')# create the pattern
matches = pattern.finditer(test_string)
for match in matches:
    print(match.group())

####################################Quantifier#########
test_string = 'hello123_ heyho hohey'
pattern = re.compile(r'\d*')# create the pattern
#pattern = re.compile(r'\d+')# create the pattern
#pattern = re.compile(r'_\d')# create the pattern
#pattern = re.compile(r'_?\d')# create the pattern
#pattern = re.compile(r'\d{2}')# create the pattern
#pattern = re.compile(r'\d{1,3}')# create the pattern
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
#################################Example###########
dates = '''
01.04.2020
2020.05.06
2020-06-04
2020-12-01
2020-03-02
2020-07-31
2020/08/08
2020_06_04
2020_04_06
'''
#pattern = re.compile(r'\d\d\d\d-\d\d-\d\d')# create the pattern
#pattern = re.compile(r'\d\d\d\d[-/.]\d\d[-/.]\d\d')# create the pattern
#pattern = re.compile(r'\d{4}[-/.]\d{2}[-/.]\d{2}')# create the pattern
#pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')# create the pattern
pattern = re.compile(r'\d\d\d\d.0[56].\d\d')# create the pattern
matches = pattern.finditer(dates)
for match in matches:
    print(match)

###############################Example######Grouping####
import re
my_string = '''
Hello World
123
2020/05/20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms. Smith
Mr. T
Pythonengineer@gmail.com
Python-engineer@gmx.de
Python-enginer123@my-domain.org
'''

#pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+') #(Mr or Ms or Mrs)<-- grouping  \.? <-- with a period (optional) \s<-- whitespace \w+ <-- alphanumeric 1 or more times
#pattern = re.compile(r'[a-zA-z\d-]+@\w+.\w+')
#pattern = re.compile(r'[a-zA-z\d-]+@[a-zA-z-]+\.(com|de|org)')
pattern = re.compile(r'([a-zA-z\d-]+)@([a-zA-z-]+)\.([a-zA-z]+)') #<-- print(match.group(1)) specify which group you want to print out
matches = pattern.finditer(my_string)

for match in matches:
    #print(match.group(0))
    #print(match.group(1))
    #print(match.group(2))
    print(match.group(3))


#############SUB############SPLIT#####
#modifying split() and sub()
urls = '''
http://python-engineer.com
https://www.python-engineer.com
http://www.pyeng.net

'''
pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-z]+)')
sub_string = pattern.sub(r'\2\3',urls)
print(sub_string)
#test_string = '123abc456789abc123ABC'
#test_string1 = 'hello World, you are the best world'
#pattern = re.compile(r'world')
#sub_string = pattern.sub('planet', test_string1)
#pattern = re.compile(r'abc')
#splited = pattern.split(test_string)
#print(splited)
#print(sub_string)

##########codewars challenge######
import re
string = 'O tempora o mores !'
def pig_it(string):
    pattern = re.compile(r'(\w{1})(\w*)')
    sub = re.sub(pattern,r'\2\1ay',string)
    return sub


print(pig_it(string))

################https://dev.to/awwsmm/20-small-steps-to-become-a-regex-master-mpc#####
import re
string = '42L 12 x 3.4f 6l 3.3 0F L F .2F 0'
pattern = re.compile(r'\d*\.?\d[fFlL]?')
matches = pattern.finditer(string)
for match in matches:
    print(match)

import re
string = '42L 12 x 3.4f 6l 3.3 0F L F .2F 0'
pattern = re.compile(r'[0-9]+\.?[a-zA-Z]|[0-9]+\.[0-9]f?|\.[0-9]F|[0-9]+')
matches = pattern.finditer(string)
for match in matches:
    print(match)

#######Pig latin#####
def pig_it(string):
    pattern = re.compile(r'(\w*)(\w{1})')
    sub = pattern.sub(r'\2\1',string)
    return sub


print(pig_it(string))