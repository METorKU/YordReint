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
print(onoff)
print("mode",mode)
global modes
modes = {1:10,2:20,3:30}
all7= [a,b,c,d,e,f,g]
dict1 = {0: [1,1,1,1,1,1,0], 1: [0,1,1,0,0,0,0], 2: [1,1,0,1,1,0,1], 
3: [1,1,1,1,0,0,1], 4: [0,1,1,0,0,1,1], 5: [1,0,1,1,0,1,1], 
6: [1,0,1,1,1,1,1,], 7: [1,1,1,0,0,0,0], 8: [1,1,1,1,1,1,1], 9: [1,0,1,0,0,1,1]}
GPIO.output(d2, 1)
for i in range(7):
    GPIO.output(all7[i], abs(dict1[1][i]-1) )

#select mode with button
def selectmode(mode, blink):
    while True:
        if GPIO.event_detected(17):
            starttime = time.time()
            end = 0
            while GPIO.input(17) == 1:
                end = time.time() - starttime
            print(end)
            if end < 1:
                if mode == 1:
                    mode = 2
                elif mode == 2:
                    mode = 3
                else:
                    mode = 1 
                sleep(0.5)
                for i in all7:
                    GPIO.output(i, 1)
                for i in range(7):
                    GPIO.output(all7[i], abs(dict1[mode][i]-1))
                print("mode", mode)
            if end > 1:
                blink = modes[mode]
                onoff = "on"
                print(onoff, mode)
                return mode, blink, onoff

#important. used in detecting coin
def incoming(pin):
  global impulse
  global i
  impulse+=1
  i = 0
GPIO.add_event_callback(4, incoming)

while True:
    i = 0
    impulse = 0
    total = 0
    GPIO.output(5, 0)
    print("i'm back")
#call mode select function
    m = selectmode(mode,modes[mode])
#next 3 variables recieved from return value of function, set to something else if not using function
    mode = m[0]
    blink = m[1]
    onoff = m[2]
    GPIO.output(d1, 0)
    GPIO.output(d2, 0)
    for i in all7:
        GPIO.output(i, 1)
#coin machine code start
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
        if total >= 30 and mode == 1:
            break
        if total >= 20 and (mode == 2 or mode == 3):
            break
        sleep(0.01)
    GPIO.output(d2, 0)
    GPIO.output(d1, 0)
    for i in all7:
        GPIO.output(i,1)
#coin machine code ends
#7 seg count down code starts, uses the variable "blink" 
    if onoff == "on":
        for num in range(blink,0,-1):
            t = time.time()
            print(num)
            while time.time() - t < 0.5:
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
#countdown code ends
#reset to default code starts
        GPIO.output(d1, 1)
        GPIO.output(d2, 1)
        for i in all7:
            GPIO.output(i, 0)
        sleep(0.5)
        GPIO.output(d1, 0)
        GPIO.output(d2, 0)
        for i in all7:
            GPIO.output(i, 1)
        sleep(0.5)
        onoff = "off"
        mode = 3
        print(onoff, mode)
        GPIO.output(d2, 1)
        for i in range(7):
            GPIO.output(all7[i], abs(dict1[1][i]-1) )
#reset to default ends
    

            