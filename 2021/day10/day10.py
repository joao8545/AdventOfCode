


with open('day10_input') as file:
	data=file.readlines()

for i in range(len(data)):
    data[i]=data[i].strip('\n')

checker=[]
points=0
corrupted=[]
for j in range(len(data)):
    line=data[j]
    for i in range(len(line)):
        el=line[i]
        if el in ['(','<','{','[']:
            checker.append(el)
        if el=='}':
            if checker[-1]=='{':
                checker.pop()
            else:
                points+=1197
                corrupted.append(j)
                break
        if el==']':
            if checker[-1]=='[':
                checker.pop()
            else:
                points+=57
                corrupted.append(j)
                break
        if el==')':
            if checker[-1]=='(':
                checker.pop()
            else:
                points+=3
                corrupted.append(j)
                break
        if el=='>':
            if checker[-1]=='<':
                checker.pop()
            else:
                points+=25137
                corrupted.append(j)
                break
print(points)

list_points=[]
#print(corrupted)
for j in range(len(data)):
    points=0
    if j in corrupted:
        continue
    line=data[j]
    #print(line)
    checker=[]
    for i in range(len(line)):
        el=line[i]
        if el in ['(','<','{','[']:
            checker.append(el)
        if el=='}':
            if checker[-1]=='{':
                checker.pop()
        if el==']':
            if checker[-1]=='[':
                checker.pop()
        if el==')':
            if checker[-1]=='(':
                checker.pop()
        if el=='>':
            if checker[-1]=='<':
                checker.pop()
    for el in reversed(checker):
        points*=5
        if el =="(":
            points+=1
        if el =="[":
            points+=2
        if el =="{":
            points+=3
        if el =="<":
            points+=4
    list_points.append(points)
list_points.sort()
print(list_points[len(list_points)//2])

    
    #print(checker)