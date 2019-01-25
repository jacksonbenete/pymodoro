#!/usr/bin/python

import sys
import pynotify
#import subprocess
import os
import time

if __name__ == '__main__':
	if not pynotify.init ("icon-summary-body"):
		sys.exit (1)
	
	n = 30
	nmins = 60 * n
	for x in range(nmins, 0, -1):
		if ((x/60)%2 == 0):
			sys.stdout.write('\r'+str(x/60) + ' mins left...')
			sys.stdout.flush()
		time.sleep(1)

	# Mensagem
	n = pynotify.Notification ("REALIZE UMA PAUSA",
				   "O Pomodoro de " + n + " minutos acabou",
				   "notification-display-brightness-off")
	n.show ()
	#subprocess.call(['/usr/bin/canberra-gtk-play','--id','bell'])
	#os.popen("canberra-gtk-play --file=" +
	#	os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sounds/sound.ogg') + 
	#	" > /dev/null 2>&1 || true")

	duration = 0.1  # second
	freq = 440  # Hz
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

	