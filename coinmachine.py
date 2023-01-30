import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()
 
i = 0
impulse = 0
#variable total contains total baht 
total = 0

def incoming(pin):
    global impulse
    global i
    impulse+=1
    i = 0

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
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(5, GPIO.OUT)
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
GPIO.add_event_detect(4, GPIO.RISING)
GPIO.add_event_callback(4, incoming)
global all7
all7= [a,b,c,d,e,f,g]
global dict1
dict1 = {0: [1,1,1,1,1,1,0], 1: [0,1,1,0,0,0,0], 2: [1,1,0,1,1,0,1], 
3: [1,1,1,1,0,0,1], 4: [0,1,1,0,0,1,1], 5: [1,0,1,1,0,1,1], 
6: [1,0,1,1,1,1,1,], 7: [1,1,1,0,0,0,0], 8: [1,1,1,1,1,1,1], 9: [1,0,1,0,0,1,1]}
##########
mode = None
#########
GPIO.output(d1, 0)
GPIO.output(d2, 0)
for i in all7:
    GPIO.output(i, 1)
while True:
    i+=1
    print("i=", i, " impulses: ",impulse, " total ", total)  
    GPIO.output(d1, GPIO.HIGH)
    ind = 0
    for j in all7:
        if total >= 10:
            GPIO.output(j, abs(dict1[int(str(total)[0])][ind] - 1))
            ind += 1
        if total < 10:
            GPIO.output(j, 1)
            ind += 1
    sleep(0.01)
    GPIO.output(d1, GPIO.LOW)
    ind = 0
    for j in all7:
        GPIO.output(j, 1)
        ind += 1
    GPIO.output(d2, GPIO.HIGH)
    ind = 0
    for j in all7:
        if total >= 10:
            GPIO.output(j, abs(dict1[int(str(total)[1])][ind] - 1))
            ind += 1
        if total < 10:
            GPIO.output(j, abs(dict1[total][ind] - 1))
            ind += 1
    if i>=30 and impulse>45:
        total+=10
        impulse = 0
        for i in all7:
            GPIO.output(i, 1)
    if i>=30 and impulse<=45 and impulse>20:
        total+=5
        impulse = 0
        for i in all7:
            GPIO.output(i, 1)
    if total >= 30 and mode == "Power wash":
        break
    if total >= 20 and (mode == "Quick wash" or mode == "Delicates"):
        break
    sleep(0.01)
GPIO.output(d2, 0)
GPIO.output(d1, 0)
for i in all7:
    GPIO.output(i,1)