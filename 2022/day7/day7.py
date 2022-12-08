import AoCutils
import os



class Dir:
    def __init__(self,parent=None,name='', children=[],size=0,level=0) -> None:
        self.parent=parent
        self.name=name
        self.children=children
        self.size=size
        self.level=level
        if self.parent!=None:
            #print(f"{self.name} added to {self.parent.name}")
            self.parent.add_dir(self)
            
    def __lt__(self, other):
         return self.size < other.size
     
    def add_file(self,file):
        self.children.append(file)
        self.size+=file.size
        if self.parent!= None:
            self.parent.update_size(file.size)
    
    def add_dir(self,dir):
        self.children.append(dir)
    
    def update_size(self,f_size):
        self.size+=f_size
        if self.parent!= None:
            self.parent.update_size(f_size)
            
    def __repr__(self) -> str:
        return f"dir {self.name} with size {self.size} at level {self.level} contains {[c.name for c in self.children]}"
         
    
    def print(self):
        print(f"{'-'*self.level} {self.name}")
        for c in self.children:
            c.print()
    def print_children():
        pass

class File:
    def __init__(self,parent:Dir,size,name) -> None:
        self.size=size
        self.name= name
        self.parent=parent
        self.parent.add_file(self)
    
    def __repr__(self) -> str:
        return f"file {self.name} with size {self.size} with parent {self.parent}"
    def print(self):
        print(f"{'-'*(self.parent.level+1)} {self.name}")
        



lines= AoCutils.start_puzzle(day=7,dir=os.path.dirname(__file__))

directories=[]
curr_idx=0
curr_dir=None
total_space=70000000
#lines= AoCutils.load_test(day=7,dir=os.path.dirname(__file__))
for line in lines:
    inp=line.split(' ')
    if inp[0]=='$':
        #print(line)
        if inp[1]=='cd' and inp[2]!='..':
            directories.insert(curr_idx,Dir(curr_dir,inp[2],children=[],level=0 if curr_dir==None else curr_dir.level+1))
            #print(f"{inp[2]} add to {curr_dir.name if curr_dir!=None else 'root'} at {curr_idx}")
            curr_dir=directories[curr_idx]
            curr_idx+=1
        elif inp[1]=='cd' and inp[2]=='..':
            #curr_idx-=1
            #curr_dir=directories[curr_idx]
            #print(f'moved up from {curr_dir} to {curr_dir.parent}')
            curr_dir=curr_dir.parent
            
    else:
        if inp[0]!='dir':
            f=File(curr_dir,int(inp[0]),inp[1])
            

#directories[0].print()
           
#print(directories[0]) 
free_space=total_space-directories[0].size    
directories.sort()
s=0
for dir in directories:
    if dir.size<=100000:
        s+=dir.size
    else:
        break

for dir in directories:
    if dir.size<30000000-free_space:
        continue
    else:
        print("p2",dir.size)
        break

print(s)
#print (lines)