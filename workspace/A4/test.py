import SoundDetector   #Change this to test parts 1-3
import loadTestCases
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import math
from scipy.signal import get_window
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import stft as STFT
import utilFunctions as UF
eps = np.finfo(float).eps

'''
#---------------Part1
dictionary = loadTestCases.load(1,2)
input = dictionary['input']
M = input['M']
window = input['window']
output = dictionary['output']


myoutput = A4Part1.extractMainLobe(window, M)
'''


'''
#----------------Part 2
dictionary = loadTestCases.load(2,3)
input = dictionary['input']
inputFile = input['inputFile']
window = input['window']
M = input['M']
N = input['N']
H = input['H']
output = dictionary['output']

myoutput = A4Part2.computeSNR(inputFile, window, M, N, H)
'''





#inputFile = '../../sounds/piano.wav'
#window = 'blackman'
#M = 513
#N = 1024
#H = 128

#envelope = A4Part3.computeEngEnv(inputFile, window, M, N, H)

#--------------Part 4
#dictionary = loadTestCases.load(4,1)
#input = dictionary['input']
#inputFile = input['inputFile']
#window = input['window']
#M = input['M']
#N = input['N']
#H = input['H']
#output = dictionary['output']
#odf = A4Part4.computeODF(inputFile, window, M, N, H)


inputFile = './PS/PS_LLL_1.wav'
window = 'blackman'
M = 513
N = 1024
H = 128
odf = SoundDetector.computeODF(inputFile, window, M, N, H)





#plt.plot(np.arange(-hN,hN)/float(N)*M,mX1-max(mX1))
#plt.axis([-20,20,-80,0])
#plt.show()
