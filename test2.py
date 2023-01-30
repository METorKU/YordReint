import RPi.GPIO as GPIO
from time import sleep

 
#variable total contains total baht 



GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.add_event_detect(4, GPIO.RISING)


##########
mode = None
#########
def coindetect(mode):
    def incoming(pin):
        global impulse
        global i
        impulse+=1
        i = 0
    global i
    i = 0
    global impulse
    impulse = 0
    total = 0
    GPIO.add_event_callback(4, incoming)
    while True:
        i+=1
        print("i=", i, " impulses: ",impulse, " total ", total)  
        if i>=30 and impulse>7:
            total+=10
            impulse = 0
        elif i>=30 and impulse<=7 and impulse>2:
            total+=5
            impulse = 0
        elif total >= 30 and mode == "Power wash":
            break
        elif total >= 20 and (mode == "Quick wash" or mode == "Delicates"):
            break
        sleep(0.01)

coindetect("Quick wash")