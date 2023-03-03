import RPi.GPIO as GPIO
from time import sleep

onoff = "off"
startstop = "stop"
blink = 10
#PINS
#4: LED RED
#22: LED BLUE
#17: start/stop
#27: power
#23: digit1
#24: digit2
a = 13
b = 26
c = 16
d = 21
e = 20
f = 19
g = 6
d1 = 23
d2 = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
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

while True:
    if GPIO.event_detected(27):
        if onoff == "off":
            onoff = "on"
            print(onoff)
        else:
            onoff = "off"
            print(onoff)
    if onoff == "on":
        GPIO.output(4,GPIO.HIGH)
        if GPIO.event_detected(17) and onoff == "on":
            if startstop == "start":
                startstop = "stop"
            else:
                startstop = "start"
        if startstop == "start":
            for i in range(blink):
                print(blink)
                if GPIO.event_detected(17):
                    print("paused")
                    startstop = "stop"
                    break
                GPIO.output(22,GPIO.HIGH)
                sleep(0.3)
                GPIO.output(22,GPIO.LOW)
                sleep(0.3)
                blink -= 1
            if blink == 0:
                startstop = "stop"
                blink = 10
        elif startstop == "stop":
            if GPIO.event_detected(25):
                onoff = "off"
            GPIO.output(22,GPIO.LOW)
    elif onoff == "off":
        GPIO.output(4,GPIO.LOW)
        startstop = "stop"
        GPIO.output(22,GPIO.LOW)
        blink = 10
