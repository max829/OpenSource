import RPi.GPIO as GPIO
import time
 
pin = 18 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0
try:
    print(1)
    p.ChangeDutyCycle(7.5)
    print(2)
    #print "angle : 8"
    time.sleep(10)
    print(3)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()
