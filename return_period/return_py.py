
import numpy as np
import scipy
from scipy import stats
import matplotlib.pylab as plt
from mpldatacursor import datacursor

#Define set values
g = 9.81;
Dt = np.divide(1.,12.)
Cltresh = 0.05
extremeMarks = np.array(np.hstack((100, 50., 25., 10., 5., 1., .1)))
filename = 'monthlyExtreme1.txt'

#Import data
data = np.genfromtxt(filename, delimiter=" ")
Hmo = data[:,4]

#initialize valuesR
N = len(Hmo)
Fm = 1.-np.divide(np.arange(1., (N)+1), N+1.)
Trm = np.divide(Dt, (1 - Fm))

#Hmo analyses
Hmo = np.sort(Hmo)[::-1]
HmoMean = np.mean(Hmo)
HmoStdDev = np.std(Hmo)
Tp = 15.66*np.sqrt(np.divide(Hmo, g))

Ath = np.multiply(0.78, HmoStdDev)
Bth = HmoMean - np.multiply(0.45, HmoStdDev)

#Gumbel linear curve fit and confidence hyperbolas
Pp = -np.log((-np.log(Fm))).conj().T
p = np.polyfit(Pp, Hmo, 1.)
Hmofit = np.polyval(p, Pp)
A = p[0]
B = p[1]

STC = np.sum(((Hmo-HmoMean)**2))
SCR = np.sum(((Hmo-Hmofit)**2))
R2 = 1. - np.divide(SCR, STC)

s2res = np.divide(SCR, (N-2.))
PpMean = np.mean(Pp)
SFp2 = np.sum((Pp - PpMean)**2.)
tstudent = stats.t.ppf((1.-Cltresh/2.), (N-2.))

dTyrs = (100 - np.multiply(Dt, 1.001))/9999
Tyrs = np.arange(100., (np.multiply(Dt, 1.001))+(-dTyrs), -dTyrs)
Fyrs = 1 - np.divide(Dt, Tyrs)
Fp = -np.log(-np.log(Fyrs)).conj().T

HmoTyrs = np.multiply(A,Fp) + B
Tpyrs = 15.66*np.sqrt(np.divide(HmoTyrs, g))

srescl = np.sqrt(np.dot(s2res, 1.+1./N+np.divide((Fp-PpMean)**2., SFp2)))
CLHmo_up = HmoTyrs+np.dot(srescl, tstudent)
CLHmo_down = HmoTyrs-np.multiply(srescl, tstudent)
#%  Lower CL of Hs
CLTp_up = 15.66*np.sqrt(np.divide(CLHmo_up, g))
CLTp_down = 15.66*np.sqrt(np.divide(CLHmo_down, g))

#Plot distribution of Hs
plt.figure(num=1, figsize=(15, 5))
#plt.figure(1.)
plt.hold(True)
plt.plot(Pp, Hmo, 'b.', label="data")
gum = plt.plot(Fp, HmoTyrs, 'k-', label="Gumbel fit")
plt.plot(Fp,CLHmo_up, 'k-.', label="95% CL")
plt.plot(Fp,CLHmo_down, 'k-.')
legend = plt.legend(loc='lower right', shadow=True)

exceedFreq = 1 - np.divide(Dt,extremeMarks)
exceedFreqp = -np.log((-np.log(exceedFreq)))
plt.xticks(np.sort(exceedFreqp), np.sort(extremeMarks), fontsize=10)
plt.yticks(fontsize=10)
plt.grid()

plt.xlabel('Tr(y)', fontsize=12)
plt.ylabel('Hs(m)', fontsize=12)
plt.title('Return Period Wave Height | Location: 15.50, -97.00')
plt.hold(False)
plt.savefig('fig.png')
#datacursor()
plt.show()
#Calculate extreme values
Fext = 1 - np.divide(Dt, extremeMarks)
Fextp = -np.log((-np.log(Fext))).conj().T
Hmoext = np.dot(A, Fextp)+B
Tpext = 15.66*np.sqrt(np.divide(Hmoext, g))

# Tp values for data based on FDS assumption
sresext = np.sqrt(np.dot(s2res, 1.+1./N+np.divide((Fextp-PpMean)**2., SFp2)))
CLHmo_upext = Hmoext+np.dot(sresext, tstudent)
CLTp_upext = 15.66*np.sqrt(np.divide(CLHmo_upext, g))
#Upper CL of Hs
filename = 'extremeinfo.txt'
fid = open(filename,'w')
outs = 'Tr (y) Hs (m)   Tp (s)   CL95 Hs (m) CL95 Tp (s)\n'
fid.write(outs)
for k in np.arange(1.,8.0):
    out = np.array(np.hstack((extremeMarks[int(k)-1],
    Hmoext[int(k)-1], Tpext[int(k)-1], CLHmo_upext[int(k)-1],
    CLTp_upext[int(k)-1])))
    #fid.write(str(out)+"\n")
    print out
fid.close()
