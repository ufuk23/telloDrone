from gtts import gTTS
import os
tts = gTTS(text='I am taking off', lang='en')
tts.save("takeOff.mp3")
os.system("takeOff.mp3")

tts = gTTS(text='I am landing', lang='en')
tts.save("landing.mp3")
os.system("landing.mp3")

tts = gTTS(text='I am turning right', lang='en')
tts.save("turnRight.mp3")
os.system("turnRight.mp3")

tts = gTTS(text='I am turning left', lang='en')
tts.save("turnLeft.mp3")
os.system("turnLeft.mp3")