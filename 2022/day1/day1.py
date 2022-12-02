
with open("day1_input",'r') as file:
    content=file.readlines()
print(len(content))

backpack=[]
curr_cal=0
for line in content:
    if line=="\n":
        backpack.append(curr_cal)
        curr_cal=0
        continue
    curr_cal+=int(line)
backpack.sort()
print(sum(backpack[-3:]))