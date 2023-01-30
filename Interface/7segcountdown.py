import RPi.GPIO as GPIO
import time
from time import sleep

onoff = "off"
global mode
mode = 1
a = 13
b = 26
c = 16
d = 21
e = 20
f = 19
g = 6
d1 = 24
d2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(4, GPIO.RISING)
GPIO.setup(22,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(a, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(b,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(c, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(d,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(e, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(f,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(g,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(d1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(d2,GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(17, GPIO.RISING) 
GPIO.add_event_detect(27,GPIO.RISING)

all7= [a,b,c,d,e,f,g]
dict1 = {0: [1,1,1,1,1,1,0], 1: [0,1,1,0,0,0,0], 2: [1,1,0,1,1,0,1], 
3: [1,1,1,1,0,0,1], 4: [0,1,1,0,0,1,1], 5: [1,0,1,1,0,1,1], 
6: [1,0,1,1,1,1,1,], 7: [1,1,1,0,0,0,0], 8: [1,1,1,1,1,1,1], 9: [1,0,1,0,0,1,1]}
GPIO.output(d2, 1)
for i in range(7):
    GPIO.output(all7[i], abs(dict1[1][i]-1) )

GPIO.output(5,GPIO.LOW)
def count(blink):
    for num in range(blink,0,-1):
        t = time.time()
        print(num)
        while time.time() - t < 1:
            GPIO.output(d1, GPIO.HIGH)
            ind = 0
            for i in all7:
                if num >= 10:
                    GPIO.output(i, abs(dict1[int(str(num)[0])][ind] - 1))
                    ind += 1
                if num < 10:
                    GPIO.output(i, 1)
                    ind += 1
            sleep(0.01)
            GPIO.output(d1, GPIO.LOW)
            ind = 0
            for i in all7:
                GPIO.output(i, 1)
                ind += 1
            GPIO.output(d2, GPIO.HIGH)
            ind = 0
            for i in all7:
                if num >= 10:
                    GPIO.output(i, abs(dict1[int(str(num)[1])][ind] - 1))
                    ind += 1
                if num < 10:
                    GPIO.output(i, abs(dict1[num][ind] - 1))
                    ind += 1
            sleep(0.01)
            GPIO.output(d2, GPIO.LOW)
            ind = 0
            for i in all7:
                GPIO.output(i, 1)
                ind += 1

count(10)