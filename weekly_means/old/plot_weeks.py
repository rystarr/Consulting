import matplotlib.pyplot as plt 

week = []
hs = []
tp = []
wvd = []
ws = []
ud = []

filename = 'weekly_avg.txt'

with open(filename, 'r') as lines: 
	for line in lines: 
		data = line.rstrip().lstrip().split(",")
		weeks = data[0]
		h = data[1]
		t = data[2]
		d = data[3]
		w = data[4]
		wd = data[5]
		week.append(float(weeks))
		hs.append(float(h))
		tp.append(t)
		wvd.append(d)
		ws.append(w)
		ud.append(wd)

plt.figure(figsize=(15,5))
plt.bar(week,wvd, label='Wave Direction(deg)')
plt.xticks(week)

plot_title = "Weekly Averages: 1979-2015 | Location: -55.50, 64.00" 
plt.title(plot_title)
plt.legend(loc=2, prop={'size':8})

plt.savefig("weekly_wavedir.png")
#plt.show()