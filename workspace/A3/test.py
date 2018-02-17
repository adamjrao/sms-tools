import loadTestCases
dictionary = loadTestCases.load(4,1)
input = dictionary['input']
x = input['x']
fs = input['fs']
N = input['N']
output = dictionary['output']
[yexpect, yfiltexpect] = output

import A3Part4
[mX, mXfilt, y, yfilt] = A3Part4.suppressFreqDFTmodel(x,fs,N)






#import loadTestCases
#dictionary = loadTestCases.load(3,2)
#input = dictionary['input']
#x = input['x']
#output = dictionary['output']

#import A3Part3
#[isReal, dftbuffer, X] = A3Part3.testRealEven(x)




#----------------------------Part 2

#import loadTestCases
#dictionary = loadTestCases.load(2,1)
#input = dictionary['input']
#x = input['x']
#fs = input['fs']
#f = input['f']
#output = dictionary['output']

#import A3Part2
#mX = A3Part2.optimalZeropad(x, fs, f)


#------------------------------Part1

#dictionary = loadTestCases.load(1,1)
#input = dictionary['input']
#x = input['x']
#fs = input['fs']
#f1 = input['f1']
#f2 = input['f2']
#output = dictionary['output']

#import A3Part1
#mX = A3Part1.minimizeEnergySpreadDFT(x, fs, f1, f2)

#import numpy as np
#A = .8
#fa = 80
#phi = np.pi/2
#fs = 10000
#t = np.arange (-.002,.05,1.0/fs)
#y = A * np.cos(2 * np.pi * fa * t + phi)

