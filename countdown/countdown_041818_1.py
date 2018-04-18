# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 countdown_041818_1.py COUNTDOWNTIME
# python3 countdown_041818_1.py 60
# python3 countdown_041818_1.py 3

import time,subprocess,sys

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

#####################################
# COMMAND LINE
#####################################

user_input_countdown = sys.argv[1] # "COUNTDOWNTIME" is n = 1
logging.debug('user_input_countdown is:  %s' % str(user_input_countdown))

#####################################
# END COMMAND LINE
#####################################

timeLeft = int(user_input_countdown) # ensure that it is definitely an integer with int()
logging.debug('Time Left Input:  %s' % str(timeLeft))

while timeLeft > 0:
	print(timeLeft,end='')
	logging.debug('Current Time Left:  %s' % str(timeLeft))
	time.sleep(1)
	logging.debug("Pause")
	timeLeft = timeLeft - 1
	logging.debug('New Time Left:  %s' % str(timeLeft))

# at end of countdown, play sound file
# subprocess.Popen(['open','-a /Applications/VLC.app/Contents/MacOS/VLC','alarm.wav'],shell=True)
# subprocess.call(['/Applications/VLC.app/Contents/MacOS/VLC','--intf ncurses', 'alarm.wav'],shell=True)
subprocess.call(['/Applications/VLC.app/Contents/MacOS/VLC /Users/sunnyair/Dropbox/python_projects/countdown_041818_1/countdown/alarm.wav'],shell=True)

