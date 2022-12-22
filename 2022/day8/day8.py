import AoCutils
import os


lines= AoCutils.start_puzzle(day=8,dir=os.path.dirname(__file__))
#lines=AoCutils.load_test(8)
NUM_COL=len(lines[0])
NUM_ROW=len(lines)
visible=0
trees=set()
def look_from_side(forest,side, visulized:set[tuple[int,int]]) -> int:
    s=0
    if side=='l':
        for i in range(len(forest)):
            tallest=-1
            for j in range(len(forest[0])):
                tree=int(forest[i][j])
                if tree>tallest:
                    tallest=tree
                    s+=0 if (i,j) in visulized else 1     
                    visulized.add((i,j))           
        return s
    elif side =="r":
        for i in range(len(forest)):
            tallest=-1
            for j in reversed(range(len(forest[0]))):
                tree=int(forest[i][j])
                if tree>tallest:
                    tallest=tree
                    s+=0 if (i,j) in visulized else 1     
                    visulized.add((i,j))           
        return s
    elif side =="t":
        for j in range(len(forest[0])):
            tallest=-1
            for i in range(len(forest)):
                tree=int(forest[i][j])
                if tree>tallest:
                    tallest=tree
                    s+=0 if (i,j) in visulized else 1     
                    visulized.add((i,j))           
        return s
    elif side =="b":
        for j in range(len(forest[0])):
            tallest=-1
            for i in reversed(range(len(forest))):
                tree=int(forest[i][j])
                if tree>tallest:
                    tallest=tree
                    s+=0 if (i,j) in visulized else 1     
                    visulized.add((i,j))           
        return s
    else:
        pass

def get_scenic_score(forest:list[str],loc:tuple[int,int])->int:
    tree=forest[loc[0]][loc[1]]
    d=0
    for i in range(loc[0]+1,len(forest)):
        curr=forest[i][loc[1]]
        if curr<tree:
            d+=1
            continue
        d+=1
        break
    #print("d ",d)
    u=0
    for i in range(loc[0]-1,-1,-1):
        curr=forest[i][loc[1]]
        if curr<tree:
            u+=1
            continue
        u+=1
        break
    #print("u ",u)
    r=0
    for i in range(loc[1]+1,len(forest[0])):
        curr=forest[loc[0]][i]
        if curr<tree:
            r+=1
            continue
        r+=1
        break
    #print("r ",r)
    l=0
    for i in range(loc[1]-1,-1,-1):
        curr=forest[loc[0]][i]
        if curr<tree:
            l+=1
            continue
        l+=1
        break
    #print("l ",l)
    return l*r*u*d
        

visible+=look_from_side(lines,'l',trees)
visible+=look_from_side(lines,'r',trees)
visible+=look_from_side(lines,'t',trees)
visible+=look_from_side(lines,'b',trees)
print(visible)
scores=[]
for i in range(NUM_ROW):
    for j in range(NUM_COL):
        scores.append(get_scenic_score(lines,(i,j)))
        
print(max(scores))