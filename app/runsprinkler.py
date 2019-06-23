import RPi.GPIO as GPIO
import time
from datetime import datetime

TIME_TO_RUN = 10

def logEvent(strToLog):
        f = open("../sprinkler.log","a")
        f.write(str(datetime.now()) + " - " + strToLog + "\n")
        f.close()

def startWatering(zone, timeToRun):
	zones = [12,16,20,21]
	GPIO.setmode(GPIO.BCM)
	pinToSet = zones[zone]
	logEvent("Pin To Set : " + str(pinToSet))
	GPIO.setup(pinToSet, GPIO.OUT) 
	logEvent("Setting pin " + str(pinToSet) + " to high and sleeping for " + str(timeToRun) + " minutes")
	GPIO.output(pinToSet, 1) 
	time.sleep(timeToRun * 60) 
	logEvent("Setting pin " + str(pinToSet) + " to low and sleeping for 5 seconds")
	GPIO.output(pinToSet, 0) 
	time.sleep(5) 
	logEvent("cleaning up")
	GPIO.cleanup()

def waterAll():
	for i in range(0,4):
		startWatering(i,TIME_TO_RUN)
