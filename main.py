import os

import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
translator = google_translator()

while True:
 with sr.Microphone() as source:
     print("Speak now!")
     audio = r.listen(source)
     try:
         speech_text = r.recognize_google(audio)
         print(speech_text)
         if(speech_text =="exit"):
             break

     except sr.UnknownValueError:
         print("Couldn't understand")
     except sr.RequestError:
         print("Couldn't request results from google")

     translated_text = translator.translate(speech_text, lang_tgt='fr')
     print(translated_text)

     voice = gTTS(translated_text, lang='fr')
     voice.save("voice.mp3")
     playsound("voice.mp3")
     os.remove("voice.mp3")



