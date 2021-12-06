def cycle(init,n):
	for i in range(n):
		for j in range(len(init)):
			init[j]-=1
			if init[j]!=-1:
				init[j]=init[j]
			else:
				init[j]=6
				init.append(8)
		print(len(init),init)
	#print(len(init))


with open('day6_input') as file:
	data=file.readlines()

new_number=[0,0,0,0,0,0,0,0,0]
number=[0,0,0,0,0,0,0,0,0]

for fish in data[0].split(','):
    #print(fish)
    number[int(fish)]+=1

count = 0
while(count < 256):
    for i in range(9):
        j=i+1
        if j==9:
            j=0
        new_number[i]=number[j]
    
    new_number[6]+=number[0]
    number=new_number.copy()
    #print(new_number)
    count+=1
print(sum(number))