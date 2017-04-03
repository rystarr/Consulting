import numpy as np
import matplotlib.pylab as plt

#X = np.random.randn(100, 1)

#Open Data File
csv = np.genfromtxt('magHsSiteA.txt', delimiter=",")
Hs = csv[:,13]

#Get Dims
rows = len(Hs)
#sort descen
hs_sort = np.sort(Hs)[::-1]
rnk = np.arange(1., (rows+1))

#Probability of Exceedence
eprob = rnk/(rows+1.)

#Plot figue
plt.plot((eprob*100.), hs_sort, 'r-', linewidth=2.)
plt.xlabel('Exceedance Probability (%)', fontweight='bold')
plt.ylabel('Wave Height (m)', fontweight='bold')
plt.title('Site B', fontweight='bold')
plt.savefig('Site_B.png')
