import numpy as np
from scipy.fftpack import fft, fftshift
import math
tol = 1e-14                                                      # threshold used to compute phase

"""
A3-Part-3: Symmetry properties of the DFT

Write a function to check if the input signal is real and even using the symmetry properties of its
DFT. The function will return the result of this test, the zerophase windowed version of the input 
signal (dftbuffer), and the DFT of the dftbuffer. 

Given an input signal x of length M, do a zero phase windowing of x without any zero-padding (a 
dftbuffer, on the same lines as the fftbuffer in sms-tools). Then compute the M point DFT of the 
zero phase windowed signal and use the symmetry of the computed DFT to test if the input signal x 
is real and even. Return the result of the test, the dftbuffer computed, and the DFT of the dftbuffer. 

The input argument is a signal x of length M. The output is a tuple with three elements 
(isRealEven, dftbuffer, X), where 'isRealEven' is a boolean variable which is True if x is real 
and even, else False. dftbuffer is the M length zero phase windowed version of x. X is the M point 
DFT of the dftbuffer. 

To make the problem easier, we will use odd length input sequence in this question (M is odd). 

Due to the precision of the FFT computation, the zero values of the DFT are not zero but very small
values < 1e-12 in magnitude. For practical purposes, all values with absolute value less than 1e-6 
can be considered to be zero. Use an error tolerance of 1e-6 to compare if two floating point arrays 
are equal. 

Caveat: Use the imaginary part of the spectrum instead of the phase to check if the input signal is 
real and even.

Test case 1: If x = np.array([ 2, 3, 4, 3, 2 ]), which is a real and even signal (after zero phase 
windowing), the function returns (True, array([ 4., 3., 2., 2., 3.]), array([14.0000+0.j, 2.6180+0.j, 
0.3820+0.j, 0.3820+0.j, 2.6180+0.j])) (values are approximate)

Test case 2: If x = np.array([1, 2, 3, 4, 1, 2, 3]), which is not a even signal (after zero phase 
windowing), the function returns (False,  array([ 4.,  1.,  2.,  3.,  1.,  2.,  3.]), array([ 16.+0.j, 
2.+0.69j, 2.+3.51j, 2.-1.08j, 2.+1.08j, 2.-3.51j, 2.-0.69j])) (values are approximate)
"""

def testRealEven(x):
    """
    Inputs:
        x (numpy array)= input signal of length M (M is odd)
    Output:
        The function should return a tuple (isRealEven, dftbuffer, X)
        isRealEven (boolean) = True if the input x is real and even, and False otherwise
        dftbuffer (numpy array, possibly complex) = The M point zero phase windowed version of x 
        X (numpy array, possibly complex) = The M point DFT of dftbuffer 
    """
    M = x.size
    hN = (M//2)+1                                           # size of positive spectrum, it includes sample 0
    hM1 = (M+1)//2                                          # half analysis window size by rounding
    hM2 = M//2                                         # half analysis window size by floor
    dftbuffer = np.zeros(M)                                 # initialize buffer for DFT
    dftbuffer[:hM1] = x[hM2:]                               # zero-phase window in dftbuffer
    dftbuffer[-hM2:] = x[:hM2]
    X = np.array([])
    X = fft(dftbuffer)
    absX = abs(X[:hN])                                      # compute ansolute value of positive side
    absX[absX<np.finfo(float).eps] = np.finfo(float).eps    # if zeros add epsilon to handle log
    mX = 20 * np.log10(absX)                                # magnitude spectrum of positive frequencies in dB
    X[:hN].real[np.abs(X[:hN].real) < tol] = 0.0            # for phase calculation set to 0 the small values
    X[:hN].imag[np.abs(X[:hN].imag) < tol] = 0.0            # for phase calculation set to 0 the small values         
    pX = np.unwrap(np.angle(X[:hN]))                        # unwrapped phase spectrum of positive frequencies
    Ximag = X.imag

    if np.all(Ximag<tol):
        isRealEven = True
    else:
        isRealEven = False


    return isRealEven, dftbuffer, X
