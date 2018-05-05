# This file does cpu activity for a given number of seconds.
# Should run as many in parallel as there are logical cores.

import time
import sys

seconds_to_run = int(sys.argv[1])

stop_time = time.time() + seconds_to_run
while time.time() < stop_time:
   x = 2+2
