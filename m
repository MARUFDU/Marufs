a = float(input("Enter Attendence number out of 5 : "))

b = float(input("Enter 1st incourse marks out of 25: "))
c = float(input("Enter 12nd incourse marks out of 25: "))
d = float(input("Enter Final marks out of 70: "))

avrg = folat(b+c)/2

print(avrg)
summ= a + avrg + d 

if summ>=80:
    print("tour grsfe is A+ and point is   4.00" )
elif summ>=75:
    print("tour grsfe is A and point is   3.75" )
elif summ>=70:
    print("tour grsfe is A- and point is   3.50" )
elif summ>65:
    print("tour grsfe is B+ and point is   3.25" )
elif summ>=60:
    print("tour grsfe is B+ and point is   3.00" )
elif summ>=55:
    print("tour grsfe is B+ and point is   2.75" ) 
elif summ>=50:
    print("tour grsfe is B+ and point is   2.50" )
elif summ>=45:
    print("tour grsfe is B+ and point is   2.25" )
elif summ>=40:
    print("tour grsfe is B+ and point is   2.00" )
elif summ<40:
    print("tour grsfe is B+ and point is   0.00" )
----------------------------
number=[]
text=open('regex-sum-42.txt')
for line in text:
    line=line.strip()
    parts=line.split()
    for part in parts:
        if part.isdigit():
            number.append(float(part))
print('The total sum ',sum(number))
print(number)



text = open ('amth.txt')
words = list()
for line in text:
    if(not line.startswith("Applied Mathematics")):
        line=line.rstrip()
        teachers_name=line.split()
        for word in teachers_name:
            if word not in words: 
                words.append(word)

words.sort()
print(words)
------------------------------------------------------
import re
intnum= 0
fh = open("regex-sum-42.txt")
for line in fh:
    numbers = re.findall("[0-9]+",line)
   # print(numbers)
    
    if not numbers:
        continue
    else:
        for number in numbers:
            intnum= intnum+ int(number)
print( 'the total sum is = ' ,  intnum)
------------------------------------------------------
text = open ('amth.txt')
words = list()
for line in text:
    if(not line.startswith("Applied Mathematics")):
        line=line.rstrip()
        teachers_name=line.split()
        for word in teachers_name:
            if word not in words: 
                words.append(word)

words.sort()
print(words)
-----------------------------------------------------file = open('mbox.txt')

total = 0.0
count = 0
for x in file:
    if x.startswith('X-DSPAM-Confidence:'):
        print(x)
        value = float(x.split(':')[1].rstrip())
        
        total += value
        count += 1


avg = total/count


print(count)
print('Average of this values is = ', avg)
-------------------------------------------------------
file = open('mbox.txt')

count = 0 
email_list = []
for x in file:
    x = x.strip()
    if x.startswith('From '):
        count += 1
        words = x.split()
        if words[1] not in email_list:
            email_list.append(words[1])

print(count)
print(email_list)
--------------------------------------------------------

file = open('mbox-short.txt')

count = 0
email_count = {}

for x in file:
    x = x.strip()
    if x.startswith('From '):
        words = x.split()
        if words[1] in email_count:
            email_count[words[1]] += 1
        else:
            email_count[words[1]] = 1

print(email_count)
