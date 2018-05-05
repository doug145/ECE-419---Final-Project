import numpy as np
import time
import sys
import subprocess as sp

THREAD_COUNT = 4
BITS_PER_FRAME = 3
BASE = 3
PULSE_TIME = 1


#seconds_to_run = int(sys.argv[1])

def pulse_off(seconds):
   time.sleep(seconds)

def pulse_on(seconds):
   processes = []
   for p in xrange(THREAD_COUNT):
      processes.append(sp.Popen(['python', 'pulse_on.py', str(seconds) ])) 
   returns = [process.wait() for process in processes]

# Transmit a number in 3 ternary bits (3^3 = 27 permutations)
# https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python
def ternary(n):
    nums = "000"
    if n == 0:
        return nums
    index = 0
    nums = list(nums)
    while n:
        n, r = divmod(n, 3)
        nums[index] = str(r)
        index += 1
    return ''.join(reversed(nums))
    #return reversed(nums)

def ppm(x):
   # Last in frame is just separation.
   frame = np.zeros(4)
   print x
   frame[int(x)] = 1
   for t in frame:
      if(t):
          pulse_on(PULSE_TIME)
      else:
          pulse_off(PULSE_TIME)
   return frame
   
def do_sync_pulse():
   print "sync pulse"

# input sequence string   
def transmit(sequence):
   sequence = sequence.upper()
   do_sync_pulse()
   for l in sequence:
      print "Doing", l
      # Space case.
      if l == " ":
         b = ternary(26)
      else:
         b = ternary(ord(l)-65)
      # Convert letter to number
      for f in b:
         print ppm(f)
         

transmit("asdf")
      


# TEST 000
#pulse_off(3)
#pulse_on(60)
#pulse_off(2)

'''
# TEST 001
pulse_off(5)
pulse_on(8)
pulse_off(8)
pulse_on(8)
pulse_off(8)
pulse_on(8)
pulse_off(8)
pulse_on(8)
pulse_off(8)
pulse_on(8)
pulse_off(8)
'''


#for n in xrange(1,35,3):
#   pulse_on(n)
#   pulse_off(n)

#stop_time = time.time() + seconds_to_run
#while time.time() < stop_time:
#   x = 2+2
