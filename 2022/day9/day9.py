import AoCutils
import os


lines= AoCutils.load_input(day=9,dir=os.path.dirname(__file__))
#lines=AoCutils.load_test(9,os.path.dirname(__file__))
def is_touching(h:tuple[int,int],t:tuple[int,int]) ->tuple[bool,int,int]:
    if abs(h[0]-t[0])>1 or abs(h[1]-t[1])>1:
        #print("dif",h[0]-t[0],h[1]-t[1])
        d_x=(1 if h[0]-t[0]>=1 else -1) if abs(h[0]-t[0])!=0 else 0
        d_y=(1 if h[1]-t[1]>=1 else -1) if abs(h[1]-t[1])!=0 else 0
        return False,d_x,d_y
    return True,0,0

def move_tail(h:tuple[int,int],t:tuple[int,int]):
    d_x,d_y=0,0
    if t[0] < h[0]-1:
        if t[1] == h[1]:
           d_x += 1
        elif t[1] > h[1]:
            d_x += 1
            d_y -= 1
        elif t[1] < h[1]:
            d_x += 1
            d_y += 1
    elif t[0] > h[0]+1:
        if t[1] == h[1]:
            d_x -= 1
        elif t[1] > h[1]:
            d_x -= 1
            d_y -= 1
        elif t[1] < h[1]:
            d_x -= 1
            d_y += 1
    elif t[1] < h[1]-1:
        if t[0] == h[0]:
            d_y += 1
        elif t[0] < h[0]:
            d_x += 1
            d_y += 1
        elif t[0] > h[0]:
            d_x -= 1
            d_y += 1
    elif t[1] > h[1]+1:
        if t[0] == h[0]:
            d_y -= 1
        elif t[0] < h[0]:
            d_x += 1
            d_y -= 1
        elif t[0] > h[0]:
            d_x -= 1
            d_y -= 1 
    return t[0]+d_x,t[1]+d_y

visited=set()
h_x=0
h_y=0

t_x=0
t_y=0
visited.add((0,0))
rope=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
for line in lines:
    
    cmd=line.split(" ")[0]
    for _ in range(int(line.split(" ")[1])):
        
        if cmd =="R":
            rope[0]=(rope[0][0]+1,rope[0][1])
        elif cmd =="L":
            rope[0]=(rope[0][0]-1,rope[0][1])
        elif cmd =="U":
            rope[0]=(rope[0][0],rope[0][1]+1)
        elif cmd =="D":
            rope[0]=(rope[0][0],rope[0][1]-1)
        for i in range(1,10):
            t_x,t_y=move_tail(rope[i-1],rope[i])
            if  (t_x,t_y)== rope[i]:
                break
            rope[i]=(t_x,t_y)
            visited.add((rope[-1]))
            
            
print(len(visited))
            