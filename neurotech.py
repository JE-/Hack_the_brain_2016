# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 14:10:40 2016

@author: Hongbo WU, Paul Nogas
"""

import pandas as pd
import numpy as np
import pylab as pl

if __name__=='__main__':
    datafile=pd.read_csv('openBCI_2013-12-24_relaxation.txt',header=None,skiprows=1)
    ch_name=datafile.columns[1:]
    fft_channels=[]
    for i,ch in enumerate(ch_name):
        fft_channels.append(np.abs(np.fft.fft(datafile[i].values)))
#        fft_channels.append(datafile[i].values)
#        pl.figure()
#        pl.hold(True)
#        pl.title("Channel "+str(i))
#        pl.plot(fft_channels[i])
        
#    good_channels=[2]
    
def getFreqBandFromFFTData(fftsample,nsamples=512,samplefreq=250):
    """
    Gets the frequency bands (delta, theta, alpha, beta gamme) based on fft data.
    
    Parameters
    ----
    fftsample: array
        Array of *nsamples* fft transformed EEG.
    nsamples
    
    Returns
    ----
    
    Examples
    ----
    
    """
    delta=freq2ind(.5,3,nsamples,samplefreq) #38-42hz
    theta=freq2ind(3,8,nsamples,samplefreq) #3-8hz
    alpha=freq2ind(8,12,nsamples,samplefreq) #8-12hz
    beta=freq2ind(12,38,nsamples,samplefreq) #12-38hz
    gamma=freq2ind(38,42,nsamples,samplefreq) #38-42hz

    freqs=np.fft.fftfreq(nsamples)*samplefreq
    print delta, theta, alpha, beta, gamma
    freqbands={
        'delta': fftsample[delta[0]:delta[1]],
        'theta': fftsample[theta[0]:theta[1]],
        'alpha': fftsample[alpha[0]:alpha[1]],
        'beta': fftsample[beta[0]:beta[1]],
        'gamma': fftsample[gamma[0]:gamma[1]],
        'freqs' : freqs
    }
    return freqbands
    
def freq2ind(start,end,nsamples=512,samplefreq=250):
    """private function to get indices of FFT bin frequency"""
    return [int(start*nsamples/samplefreq),int(end*nsamples/samplefreq)]