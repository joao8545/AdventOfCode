with open('day1_input') as file:
	prev=None
	count=0
	for line in file.readlines():
		if prev ==None:
			prev=int(line)
			continue
		if int(line)>prev:
			count+=1
		prev=int(line)
	print(count)
with open('day1_input') as file:
	prev = None
	count =0
	data =file.readlines()
	for i in range(len(data)-2):
		current=sum(map(int,data[i:i+3]))
		if prev==None:
			prev=current
			continue
		if current>prev:
			count+=1
		prev=current
	print(count)
