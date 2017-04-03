import os, sys, datetime, commands
from datetime import date
import csv

filename = 'data.txt'

dates = []
hs = []
tp = []
mwd = []
ws = []
wdir = []

with open(filename, 'r') as lines:
	for line in lines:
		data = line.rstrip().lstrip().split(",")
		dt = str(datetime.datetime(int(data[2]), int(data[0]), int(data[1]), int(data[3])))
		h = data[4]
		t = data[5]
		wvd = data[6]
		wind = data[7]
		wnddir = data[8]
		dates.append(dt)
		hs.append(h)
		tp.append(t)
		mwd.append(wvd)
		ws.append(wind)
		wdir.append(wnddir)

#Write to file 
with open("test_data.txt", "w") as file:
	fieldnames = ['Date','WaveHeight','PeakPeriod','WaveDirection','WindSpeed','WindDirection']
	writer = csv.writer(file, delimiter=',')
	writer.writerow(fieldnames) 
	writer.writerows(zip(dates,hs,tp,mwd,ws,wdir))
