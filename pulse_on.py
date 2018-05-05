import numpy as np
import time
import sys

seconds_to_run = int(sys.argv[1])

stop_time = time.time() + seconds_to_run
while time.time() < stop_time:
   x = 2+2
