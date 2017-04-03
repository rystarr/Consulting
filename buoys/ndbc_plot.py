from dateutil.parser import parse
from dateutil import tz
from matplotlib.pyplot import *
from matplotlib import mlab, dates
import numpy as np
import urllib
import matplotlib.cm as cm

#txt = open('oct-2013_ndbc.txt','r').read()
data = urllib.urlretrieve('http://www.ndbc.noaa.gov/data/5day2/44091_5day.txt')
txt = open(data[0],'r').read()
lines = txt.split('\n')
lines = lines[2:]
times = []
heights = []
direction = []
period = []
try:
    for line in lines:
        dt = parse(line[0:16].replace(' ','-',2).replace(' ','T',1).replace(' ',':'))
        ht = line.split()[8]
        dir = line.split()[11]
        tp = line.split()[9]
        times.append(dt)
        heights.append(float(ht))
        direction.append(float(dir))
        period.append(float(tp))
except:
    pass

#set_xticklabels(['1','6','11','16','21','26','31'])
#plot(times, heights)


print times

f, (pHs, pTp, pDp) = subplots(3, 1, sharex=True, figsize=(15,10)) 
#fig, ax = subplots()
pHs.xaxis.set_major_formatter(dates.DateFormatter('%m/%d', tz=tz.tzlocal()))
f.autofmt_xdate()

pHs.set_title("Wave Buoy 44091")
#i = 200

pHs.plot(times, heights)
pTp.plot(times, period)
pDp.scatter(times, direction)

y1, y2 = pHs.get_ylim()
x1, x2 = pHs.get_xlim()
ax2 = pHs.twinx()
ax2.set_ylim(0 * 3.2808399, 5 * 3.2808399)
#ax2.set_ylim(y1 * 3.2808399, y2 * 3.2808399)
ax2.set_xlim(x1, x2)
pHs.set_ylim([0,5])
pDp.set_ylim([-5,370])
#pTp.set_ylim([5,10])

pHs.grid()
pTp.grid()
pDp.grid()

pHs.set_ylabel('Height (meters)')
pTp.set_ylabel('Period (seconds)')
pDp.set_ylabel('Direction (degrees)')

#max_xticks = 25
#xloc = MaxNLocator(max_xticks)
#pHs.xaxis.set_major_locator(xloc)

ax2.set_ylabel('Feet')


savefig('waveplot.png',facecolor=f.get_facecolor(), edgecolor='none')
#show()