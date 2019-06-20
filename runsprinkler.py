import RPi.GPIO as GPIO
import time

TIME_TO_RUN = 10


def startWatering(zone, timeToRun):
	zones = [12,16,20,21]
	GPIO.setmode(GPIO.BCM)
	pinToSet = zones[zone]
	print "Pin To Set : " + str(pinToSet)
	GPIO.setup(pinToSet, GPIO.OUT) 
	print "Setting pin " + str(pinToSet) + " to high and sleeping for " + str(timeToRun) + " minutes"
	GPIO.output(pinToSet, 1) 
	time.sleep(timeToRun * 60) 
	print "Setting pin " + str(pinToSet) + " to low and sleeping for 5 seconds"
	GPIO.output(pinToSet, 0) 
	time.sleep(5) 
	print "cleaning up"
	GPIO.cleanup()

def waterAll():
	for i in range(0,4):
		startWatering(i,TIME_TO_RUN)
