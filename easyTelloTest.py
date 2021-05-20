import speech_recognition as sr
import os
from easytello import tello
import time


drone = tello.Tello()

#drone.land()

print("land")
#drone.takeoff()
time.sleep(3)

print("land")

# Turning on stream
drone.streamon()