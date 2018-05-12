# This file is to decode messages from audio recording in realtime.
import matplotlib.pyplot as plt

import numpy as np
import scipy.io.wavfile
from scipy.signal import spectrogram,medfilt

"""
Takes a string of format xxx where each x is either 0, 1, or 2
does not check to make sure it is correct, so the caller is
responsible for that.
"""
def decode_ternary(n):
    print("----------------N: " + str(n) + " ---------------------" )
    if n == "222":
        return ' '
    return chr(9*int(n[0]) + 3*int(n[1]) + int(n[2]) + 97)

def decode(data):
  '''
  #filename = "test-001.wav"
  filename = data
  audio_sample = scipy.io.wavfile.read(filename)
  sampling_rate = audio_sample[0]
  audio_sample = audio_sample[1][:,0].astype(float)
  audio_sample = audio_sample/np.average(audio_sample)
  '''
  data = data[0]
  sampling_rate = 44100
  #udio_sample = np.array(data[0]+data[1]+data[2]) #combine 3 sections into numpy array
  #udio_sample = audio_sample/np.average(audio_sample)
  pulse_length = 10
  kernel = np.zeros(pulse_length * sampling_rate / 2048, dtype=float)
  l = len(kernel)
  kernel[:] = -1.0
  kernel[l/2:] = 1.0
  sum_vals = []
  thresh = -200000
  print "HERE: 1"
  for idx,d in enumerate(data):
    f, t, sxx = spectrogram(d,sampling_rate,nperseg=2048,noverlap=32,window='blackman')
    sxx = np.log10(sxx)
    #plt.clf()
    #plt.pcolormesh(t, f[:], sxx[:,:],cmap='Greys_r')
    #plt.ylabel('Frequency [Hz]')
    #plt.xlabel('Time [sec]')
    #plt.colorbar()
    #plt.savefig(str(idx)+".png")
    # Seconds
    freqs = np.shape(sxx)[0]
    print "F:",freqs
    compressed_freq_range = sxx[:freqs/5,:]
    compressed_freq_range = np.sum(compressed_freq_range,axis=0)
    convolved = np.convolve(kernel,compressed_freq_range)
    med_filtered = medfilt(convolved,kernel_size=31)
    plt.clf()
    plt.plot(med_filtered)
    #plt.ylim([-512,-150])
    plt.savefig(str(idx)+".png")

    sum_vals.append(np.sum(med_filtered))
  print "SUMS:", sum_vals
  pulse_position = np.argmin(sum_vals)
  #or i in range(len(data)/3):
  #   str_num = chr(data[i]) + chr(data[i+1]) + chr(data[i+2])
  #   print(decode_ternary(str_num))
  #set of three ternary bits of data
  #return tuple(data)
  #plt.plot(med_filtered)
  #plt.plot(sxx)
  #plt.show()
  print "Returning from decoder function call."
  return pulse_position
