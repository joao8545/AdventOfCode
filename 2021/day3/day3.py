import numpy as np

def get_most_common(data):
	A=np.zeros(len(data[0])-1,dtype=int)
	for line in data:
		line=line.strip('\n')
		for i in range(len(line)):
			A[i]+=int(line[i])
	return tuple(map(lambda x: str(int(x>=len(data)/2)),A))

def get_least_common(data):
	A=np.zeros(len(data[0])-1,dtype=int)
	for line in data:
		line=line.strip('\n')
		for i in range(len(line)):
			A[i]+=int(line[i])
	return tuple(map(lambda x: str(int(not(x>=len(data)/2))),A))

with open('day3_input') as file:
	data=file.readlines()
#print(data[0].encode())
A=np.zeros(len(data[0])-1,dtype=int)
print(A)
for line in data:
	line=line.strip('\n')
	for i in range(len(line)):
		A[i]+=int(line[i])
print(A)
g=tuple(map(lambda x: str(int(x>500)),A))
print(g)
e=tuple(map(lambda x: str(int(not(x>500))),A))
g=int(''.join(g),2)
e=int(''.join(e),2)
print(g,e)
print(e*g)

new_o2=data.copy()
k=0
while len(new_o2)!=1:
	mc=get_most_common(new_o2)
	print(mc)
	new_o2=list(filter(lambda x: x[k]==mc[k],new_o2))
	k+=1
print(new_o2)
print(int(new_o2[0],2))
new_co2=data.copy()
k=0
while len(new_co2)!=1:
	mc=get_least_common(new_co2)
	#print(mc)
	print(len(new_co2))
	new_co2=list(filter(lambda x: x[k]==mc[k],new_co2))
	k+=1
print(new_co2)
print(int(new_co2[0],2))
print(int(new_o2[0],2)*int(new_co2[0],2))