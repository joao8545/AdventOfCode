
#import AoCutils
import os


#lines= AoCutils.start_puzzle(day=5,dir=os.path.dirname(__file__))

with open("day6_input",'r') as file:
    content=file.readlines()

inp=content[0]
index=0
index2=0
for i in range(len(inp)):
    part=inp[i:i+4]
    if len(set(part))==4:
        index=i+4
        break
for i in range(len(inp)):
    part=inp[i:i+14]
    if len(set(part))==14:
        index2=i+14
        break



print(index)
print(index2)