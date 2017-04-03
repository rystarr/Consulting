repls = ('JAN','01'),('FEB','02'),('MAR','03'),('APR','04'),('MAY','05'),('JUN','06'),('JUL','07'), \
		('AUG','08'),('SEP','09'),('OCT','10'),('NOV','11'),('DEC','12'),(',','	')
txt = open('monthly_14s.txt','r').read()
new = reduce(lambda a, kv: a.replace(*kv),repls , txt)
filename = 'data.txt'
data = open(filename, 'w')
data.write(new)
data.close()