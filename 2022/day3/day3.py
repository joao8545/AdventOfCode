
import AoCutils
import os

lines= AoCutils.start_puzzle(day=3,dir=os.path.dirname(__file__))

total_part1=0
total_part2=0
for bag in lines:
    c1=bag[:len(bag)//2]
    c2=bag[len(bag)//2:]
    inter= ''.join(list(set(c1).intersection(set(c2))))
    p=0
    if 65<=ord(inter)<=90:
        p=ord(inter)-38
    elif 97<=ord(inter)<=122:
        p=ord(inter)-96
    total_part1+=p

for i in range(0,len(lines),3):
    e1=lines[i+0]
    e2=lines[i+1]
    e3=lines[i+2]
    inter= ''.join(list(set(e1).intersection(set(e2).intersection(set(e3)))))
    p=0
    if 65<=ord(inter)<=90:
        p=ord(inter)-38
    elif 97<=ord(inter)<=122:
        p=ord(inter)-96
    total_part2+=p
    
print(total_part1)
print(total_part2)