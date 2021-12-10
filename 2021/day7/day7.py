
def calculate_fuel(length,data):
    d={x:0 for x in range(length+1)}
    for el in data:
        d=func(d,el)
    #print(d)
    print(min(d,key=d.get),d[min(d,key=d.get)])
    
    
def func(d,el):
    for k in d.keys():
        kj=abs(el-k)
        #print(kj)
        d[k]+=sum(range(kj+1))
    #print(d)
    return d




with open('day7_input') as file:
	data=file.readlines()
print(data)
data=list(map(lambda x:int(x),data[0].split(',')))

calculate_fuel(max(data),data)