dist=dict(x=0,y=0)
with open('day2_input') as file:
	data=file.readlines()
	for line in data:
		t=tuple(line.split(' '))
		if t[0]=='forward':
			dist['x']+=int(t[1])
		elif t[0] =='up':
			dist['y']-=int(t[1])
		else:
			dist['y']+=int(t[1])
	print(dist)
	print(dist['x']*dist['y'])

dist=dict(x=0,y=0,aim=0)
with open('day2_input') as file:
	data=file.readlines()
	for line in data:
		t=tuple(line.split(' '))
		if t[0]=='forward':
			dist['x']+=int(t[1])
			dist['y']+=dist['aim']*int(t[1])
		elif t[0] =='up':
			dist['aim']-=int(t[1])
		else:
			dist['aim']+=int(t[1])
	print(dist)
	print(dist['x']*dist['y'])
