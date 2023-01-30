import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

global count
global counting

counting = 0

def firstFunction():
	global counter
	global ts
	global counting
	count = 1
	counter = 0
	ts = time.time()
	while True:
		if (count == 1):
			GPIO.wait_for_edge(17, GPIO.RISING)
			counting = 1
			counter += 1
			print("Pulse comming ! (%s)")
			ts = time.time()


def secondFunction():
	global count
	global counting
	global counter
	while True:
		cts = ts+2
		if cts<time.time():
			print("counting looks like finished with %s pulses")
			count = 0
			counting = 0
			print("payment now")
			if counter == 1:
				print("counter = 1")
			if counter == 2:
				print("counter = 2")
			if counter == 3:
				print("counter = 3")
			if counter == 4:
				print("counter = 4")
			if counter == 5:
				print("counter = 5")
			counter = 0
			count = 1
			print("ready")
		time.sleep(1)


def thirdFunction():
	while True:
		if (counting == 0):
			global ts
			ts = time.time()
			time.sleep(1)

try:
	t1 = Thread(target = firstFunction)
	t2 = Thread(target = secondFunction)
	t3 = Thread(target = thirdFunction)

	t1.start()
	t2.start()
	t3.start()

except KeyboardInterrupt:
	t1.stop()
	t2.stop()
	t3.stop()
	GPIO.cleanup()