from functools import reduce

def print_map(matrix):
    output=''
    for row in matrix:
        output+=' '.join(map(str,row))
        output+='\n'
    print(output)

def create_boarder(data):
    h_map=[]
    h_map.append([9]*(len(data[0])+2))
    for i in range(len(data)):
        h_map.append([])
        h_map[i+1].append(9)
        for j in range(len(data[i])):
            h_map[i+1].append(int(data[i][j]))
        h_map[i+1].append(9)
    h_map.append([9]*(len(data[0])+2))
    return h_map

def check_neighbours(data,point_to_check,checked):
    #return up to 4 valid points
    #check all 4 neighbours
    #add to point to check
    checked.append(point_to_check)
    x,y=point_to_check
    for i in [-1,1]:
        point=data[x+i][y]
        if (x+i,y) in checked or point==9:
            continue
        else:
            check_neighbours(data,(x+i,y),checked)

    for j in [-1,1]:
        point=data[x][y+j]
        if (x,y+j) in checked or point==9:
            continue
        else:
            check_neighbours(data,(x,y+j),checked)

    return

with open('day9_input') as file:
	data=list(map(lambda x: x.strip(),file.readlines()))

#print(data)

h_map=create_boarder(data)
low_coords=[]
low_points=[]
for i in range(len(h_map)):
    y_neighbours=[]
    if i!=0 :
        y_neighbours.append(i-1)
    if i!=len(h_map)-1:
        y_neighbours.append(i+1)
    for j in range(len(h_map[i])):
        x_neighbours=[]
        if j!=0 :
            x_neighbours.append(j-1)
        if j!=len(h_map[i])-1:
            x_neighbours.append(j+1)
        flag_low=True
        
        for ii in y_neighbours:
            for jj in x_neighbours:

                if h_map[i][j]>=h_map[ii][j] or h_map[i][j]>=h_map[i][jj]:
                    flag_low=False
               

        if flag_low:
            low_coords.append((i,j))
            low_points.append(h_map[i][j])
#print(low_points)
print(sum(low_points)+len(low_points))


basins=[]
for point in low_coords:
    checked=[]
    check_neighbours(h_map,point,checked)
    basins.append(len(checked))
basins.sort()
print(reduce(lambda x,y:x*y,basins[-3:]))
print(basins[-3:])





        
