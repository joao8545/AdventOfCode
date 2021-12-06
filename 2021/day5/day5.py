

class Line:
    def __repr__(self):
        return f'{self.start} -> {self.end}'
    def __init__(self,p1,p2):
        self.start=p1
        self.end=p2
        #print(self,self.get_len())
        pass
    def get_max_x(self):
        return max(self.start[0],self.end[0])

    def get_max_y(self):
        return max(self.start[1],self.end[1])
    
    def is_diagonal(self):
        return not(self.start[0]==self.end[0] or self.start[1]==self.end[1])

    def get_real_len(self):
        return((self.end[0]-self.start[0])**2 +(self.end[1]-self.start[1])**2)**0.5
    
    def get_len(self):
        return max(abs(self.end[0]-self.start[0]),abs(self.end[1]-self.start[1]))
    
    def get_points(self):
        p_start=(min(self.start[0],self.end[0]),min(self.start[1],self.end[1]))
        p_end=(max(self.start[0],self.end[0]),max(self.start[1],self.end[1]))
        #print(self)
        d_points=[]
        s_points=[]
        if self.is_diagonal():
            for i in range(self.get_len()+1):
                point=[self.start[0],self.start[1]]
                #print(point)
                if self.start[0]>self.end[0]:
                    point[0]-=i
                else:
                    point[0]+=i
                if self.start[1]>self.end[1]:
                    point[1]-=i
                else:
                    point[1]+=i
                d_points.append(tuple(point))
        else:
            s_points=[(x,y) for x in range(p_start[0],p_end[0]+1) for y in range(p_start[1],p_end[1]+1)]
        #print([*s_points,*d_points])
        return [*s_points,*d_points]
            




class Grid:
    def __repr__(self):
        matrix=self.board
        output=''
        for row in matrix:
            output+=' '.join(map(str,row))
            output+='\n'
        return output
    def __init__(self,x,y):
        self.height=y
        self.width=x
        self.board=[]
        for i in range(y):
            self.board.append(['.']*x)
        #print(self.board)
        pass
    
    def add_line(self,line):
        points=line.get_points()
        for point in points:
            #print(point)
            if self.board[point[1]][point[0]]=='.':
                self.board[point[1]][point[0]]=1
            else:
                self.board[point[1]][point[0]]+=1
        pass
    
    def count(self,n):
        count=0
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i]=='.':
                    continue
                if self.board[j][i]>=n:
                    count+=1
        return count

def create_lines(data):
    l=[]
    lines=[]
    for i in range(len(data)):
        l.append(list(map(lambda x: (int(x[0]),int(x[1])),map(lambda x: x.split(','),data[i].strip('\n').split(' -> ')))))
    for line in l:
        lines.append(Line(line[0],line[1]))
    return lines


with open('day5_input') as file:
	data=file.readlines()


lines=create_lines(data)


grid=Grid(max(map(lambda x:x.get_max_x(),lines))+1,max(map(lambda x:x.get_max_y(),lines))+1)
for line in lines:
    grid.add_line(line)
#print(grid)
print(grid.count(2))