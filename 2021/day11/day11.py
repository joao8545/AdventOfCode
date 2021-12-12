
class Octopus:

    def __repr__(self):
        if self.boarder:
            return ''
        return str(self.energy)

    def __init__(self,energy,boarder=False):
        self.energy=energy
        self.boarder=boarder
        self.flashed=False

    def start_step(self):
        self.flashed=False
    
    def increase_energy(self):
        if not self.flashed and not self.boarder:
            self.energy+=1
        
    def flash(self):
        if self.energy>9 and not self.boarder:
            self.flashed=True
            self.energy=0
            return True
        return False

def increase_energy(grid,i,j,counter):
    #print(counter)
    octopus=grid[i][j]
    octopus.increase_energy()
    if octopus.flash():
        counter+=1
        for ii in [-1,0,1]:
            for jj in [-1,0,1]:
                if ii==0 and jj==0:
                    continue
                counter=increase_energy(grid,i+ii,j+jj,counter)
    #print(counter)
    return counter

def print_grid(matrix):
    output=''
    for row in matrix:
        output+=' '.join(map(str,row))
        output+='\n'
    print(output)

def create_octopus_grid(data):
    h_map=[]
    h_map.append([Octopus(9,True)]*(len(data[0])+2))
    for i in range(len(data)):
        h_map.append([])
        h_map[i+1].append(Octopus(9,True))
        for j in range(len(data[i])):
            h_map[i+1].append(Octopus(int(data[i][j])))
        h_map[i+1].append(Octopus(9,True))
    h_map.append([Octopus(9,True)]*(len(data[0])+2))
    return h_map

def Check_all(grid,part1,max,steps):
    if part1:
        if steps>=max:
            return True
        return False
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[i])-1):
            if grid[i][j].energy != 0:
                return False
    return True

with open('day11_input') as file:
	data=file.readlines()

for i in range(len(data)):
    data[i]=data[i].strip('\n')
steps=0
grid=create_octopus_grid(data)
print_grid(grid)
print()
counter=0
part1=False
while True:
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[i])-1):
            octopus=grid[i][j]
            octopus.start_step()

    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[i])-1):
            counter=increase_energy(grid,i,j,counter)
    steps+=1
    if Check_all(grid,part1,100,steps):
        break
    #print_grid(grid)
print('steps',steps)
print('counter',counter)