

class Board:
    def __repr__(self):
        return str(self.id)
    def __init__(self,board_list,id=None):
        self.id=id
        self.board=[[]]
        i=0
        j=0
        #print(board_list)
        for n in board_list:
            #print(i,j,n)
            self.board[j].append([int(n),False])
            #print(self.board)
            i+=1
            if i==5:
                self.board.append([])
                i=0
                j+=1
        self.board.remove([])
        #print(len(self.board))

    def mark(self,number):
        #print(type(number))
        for i in range(5):
            for j in range(5):
                if self.board[i][j][0]==number:
                    self.board[i][j][1]=True
                    #print(self.board)
                    return
    
    def check_for_win(self):
        line=[]
        row=[]
        for i in range(5):
            for j in range(5):
                line.append(self.board[i][j][1])
                row.append(self.board[j][i][1])
            #print(line)
            #print(row)
            if all(line) or all(row):
                return True
            line=[]
            row=[]    
        return False
    
    def calculate_points(self):
        points=0
        for i in range(5):
            for j in range(5):
                if not self.board[i][j][1]:
                    points+=self.board[i][j][0]
        return points

def create_board(lines,id):
    k=[]
    for el in lines:
        k.extend(el)
    return Board(k,id)
#read data
with open('day4_input') as file:
	data=file.readlines()

number_list=list(map(lambda x:int(x),data[0].split(',')))
j=0
lines=[]
board_list=[]
id=0
for i in range(2,len(data)):
    if data[i]=='\n':
        continue
    #print(data[i])
    lines.append(filter(lambda x: x!='',data[i].strip('\n').split(' ')))
    if len(lines)==5:
        
        board_list.append(create_board(lines,id))
        #break
        id+=1
        lines=[]


flag=False
#number_list=[26,70,3,5,89]
for number in number_list:
    print(len(board_list))
    for board in board_list:
        board.mark(number)
        if board.check_for_win():
            
            print(board,board.calculate_points()*number)

            board_list.remove(board)
            #flag=True
            #break
    if flag:
        break
