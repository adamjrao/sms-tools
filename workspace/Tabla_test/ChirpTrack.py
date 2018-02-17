import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../software/models/"))
import utilFunctions as UF
import sineModel as SM

inputFile = './Tiffany_HF001_PS_LLL_1'

#window = 'hamming'
#M = 501
#N = 1024
#t = -90
#minSineDur = 0.05
#maxnSines = 20
#freqDevOffset = 10
#freqDevSlope = 0.001
#H = 200

window = 'blackmanharris'
M = 401
N = 2048
t = -90
minSineDur = 0.5
maxnSines = 30
freqDevOffset = 0
freqDevSlope = 0.01
H = 50

(fs, x) = UF.wavread(inputFile)
w = get_window(window, M)
tfreq, tmag, tphase = SM.sineModelAnal(x, fs, w, N, H, t, maxnSines, minSineDur, freqDevOffset, freqDevSlope)

numFrames = int(tfreq[:,0].size)
frmTime = H*np.arange(numFrames)/float(fs)
tfreq[tfreq<=0] = np.nan
plt.plot(frmTime, tfreq)

plt.show()
