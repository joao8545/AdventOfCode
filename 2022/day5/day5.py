
import AoCutils
import os


lines= AoCutils.start_puzzle(day=5,dir=os.path.dirname(__file__))
stacks=[]
n_stacks=[]
commands=[]
ended_stacks=False


def part1(stack,commands):
    d_stacks=stack[:]
    for cmd in commands:
        for _ in range(int(cmd[0])):
            t=d_stacks[int(cmd[1])-1].pop()
            d_stacks[int(cmd[2])-1].append(t)

    message="".join([el[-1] for el in d_stacks])
    print(message)
    
    
def part2(stack,commands):
    f_stacks=stack[:]
    for cmd in commands:
        for i in range(int(cmd[0])):
            t=f_stacks[int(cmd[1])-1].pop(len(f_stacks[int(cmd[1])-1])-int(cmd[0])+i)
            f_stacks[int(cmd[2])-1].append(t)
    message="".join([el[-1] for el in f_stacks])
    print(message)

for line in lines:
    if line=="":
        ended_stacks=True
        continue
    if ended_stacks:
        commands.append((line.split(" ")[1],line.split(" ")[3],line.split(" ")[5]))
    else:
        stacks.append(line)
    
number_of_stacks=max(list(map(lambda x: int(x) if x !="" else -1,stacks[-1].split(" "))))
stacks=stacks[:-1]
for _ in range(number_of_stacks):
    n_stacks.append([])
for line in reversed(stacks):
    for i in range(number_of_stacks*4-3,0,-4):
        if(line[i]==" "):
            continue
        n_stacks[i//4].append(line[i])

part1(n_stacks,commands)
n_stacks=[]
for _ in range(number_of_stacks):
    n_stacks.append([])
for line in reversed(stacks):
    for i in range(number_of_stacks*4-3,0,-4):
        if(line[i]==" "):
            continue
        n_stacks[i//4].append(line[i])
part2(n_stacks,commands)

    
