# This file is to decode messages from audio recording in realtime.

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
  sampling_rate = 4410
  audio_sample = np.array(data[0]+data[1]+data[2]) #combine 3 sections into numpy array
  audio_sample = audio_sample/np.average(audio_sample)

  f, t, sxx = spectrogram(audio_sample,sampling_rate,nperseg=2048,noverlap=32,window='blackman')

  sxx = np.log10(sxx)


  import matplotlib.pyplot as plt

  '''
  plt.pcolormesh(t, f[:10], sxx[:10,:],cmap='Greys_r')
  plt.ylabel('Frequency [Hz]')
  plt.xlabel('Time [sec]')
  plt.colorbar()
  plt.show()
  '''

  # Seconds
  pulse_length = 8

  kernel = np.zeros(pulse_length * sampling_rate / 2048, dtype=float)
  l = len(kernel)
  kernel[:] = -1.0
  kernel[l/2:] = 1.0

  compressed_freq_range = sxx[:,:]
  compressed_freq_range = np.sum(compressed_freq_range,axis=0)

  convolved = np.convolve(kernel,compressed_freq_range)
  print len(compressed_freq_range)
  med_filtered = medfilt(compressed_freq_range,kernel_size=177)

  #audio sample piped in as 24 second chunks
  num_sections = 3
  thresh = -200000
  section_length = len(med_filtered)/num_sections

  data = list()
  for section in range(num_sections):
    start = section_length*section
    end = section_length*(section+1)
    #print start, end
    #print med_filtered[start:end]
    sum_val = np.sum(med_filtered[start:end])
    if sum_val > thresh:
      data.append(1)
    else:
      data.append(0)
    #print sum_val

  for i in range(len(data)/3):
      str_num = chr(data[i]) + chr(data[i+1]) + chr(data[i+2])
      print(decode_ternary(str_num))

  #set of three ternary bits of data
  #return tuple(data)

  plt.plot(med_filtered)
  #plt.plot(sxx)
  plt.show()

#decode('test-001.wav')
