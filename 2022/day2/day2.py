

def calculate_score(cmd):
    scores_map={"AX":1+3,"BX":1+0,"CX":1+6,"AY":2+6,"BY":2+3,"CY":2+0,"AZ":3+0,"BZ":3+6,"CZ":3+3}
    return scores_map[cmd]

def calculate_shape(cmd):
    shapes_map={"AX":"Z","BX":"X","CX":"Y","AY":"X","BY":"Y","CY":"Z","AZ":"Y","BZ":"Z","CZ":"X"}
    return shapes_map[cmd]

with open("day2_input",'r') as file:
    content=file.readlines()
print(len(content))

total_score=0
for line in content:
    total_score+=calculate_score(''.join(line.split()))
print(total_score)

total_score=0
for line in content:
    total_score+=calculate_score(line[0]+calculate_shape(''.join(line.split())))
print(total_score)
