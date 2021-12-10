from collections import Counter

def sortString(str):
    return ''.join(sorted(str))

with open('day8_input') as file:
	data=file.readlines()

def return_digit(display,maping):
    if len(display)==2:
        return 1
    if len(display)==4:
        return 4
    if len(display)==3:
        return 7
    if len(display)==7:
        return 8
    if len(display)==6 and maping['c'] not in display:
        return 6
    if len(display)==6 and maping['e'] not in display:
        return 9
    if len(display)==6 and maping['d'] not in display:
        return 0
    if len(display)==5 and maping['b'] not in display and maping['f'] not in display:
        return 2
    if len(display)==5 and maping['b'] not in display and maping['e'] not in display:
        return 3
    if len(display)==5 and maping['c'] not in display and maping['e'] not in display:
        return 5

print(data[0].split('|')[0].split(' '))

count=0
for line in data:
    for digit in line.split('|')[1].split(' '):
        if digit =="":
            continue
        digit=digit.strip('\n')
        if len(digit) in [2,4,3,7]:
            count+=1
#print(count)
print(list(map(sortString,data[0].split('|')[0].split(' '))))
total_counter=0
for line in data:

    c=Counter(''.join(line.split('|')[0].split(' ')))
    #original:mixed
    segments={x:'.' for x in ('abcdefg')}
    digits={x:'.' for x in range(10)}

    for digit in line.split('|')[0].split(' '):
            if digit =="":
                continue
            digit=digit.strip('\n')
            if len(digit) ==2:
                digits[1]=digit
            if len(digit) ==3:
                digits[7]=digit
            if len(digit) ==4:
                digits[4]=digit
            if len(digit) ==7:
                digits[8]=digit
    for el in c:
        if c[el]==9:
            segments['f']=el
        elif c[el]==6:
            segments['b']=el
        elif c[el]==4:
            segments['e']=el
        elif c[el]==8 and not(el in digits[1]):
            segments['a']=el
        elif c[el]==8 and el in digits[1]:
            segments['c']=el
        elif c[el]==7 and el in digits[4]:
            segments['d']=el
        elif c[el]==7 and not(el in digits[4]):
            segments['g']=el
        else:
            print('error on',el)
    
    displays=line.split('|')[1].split(' ')
    displays.remove('')
    display_count=0
    for i in range(len(displays)):
        displays[i]=displays[i].strip()
        #print(return_digit(displays[i],segments), end=' ')
        display_count+=return_digit(displays[i],segments)*10**(3-i)
    #print("\n",display_count)
    total_counter+=display_count
        
print(total_counter) 
    

