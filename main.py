import speech_recognition as sr
import os
from easytello import tello
import time



#drone = tello.Tello()

#drone.land()

print("land")
#drone.takeoff()
time.sleep(8)

print("land")



r = sr.Recognizer()
mic = sr.Microphone()

while True:
    try:
        with mic as audio_file:
            print("Speak Please")
            r.pause_threshold = 2
            r.adjust_for_ambient_noise(audio_file, duration=0.1)
            audio = r.listen(audio_file, phrase_time_limit=10)
            print("Converting Speech to Text...")
            speech = r.recognize_google(audio, language='en-in')
            print("You said: " + speech)

            if speech.lower().startswith("land"):
                os.system("landing.mp3")
                drone.land()
            elif speech.lower().startswith("takeoff") or speech.lower().startswith("take off"):
                os.system("takeOff.mp3")
                drone.takeoff()
            elif speech.lower().startswith("turn left"):
                os.system("turnLeft.mp3")
            elif speech.lower().startswith("turn right"):
                os.system("turnRight.mp3")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown speech")