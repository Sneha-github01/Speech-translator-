import os
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
translator = Translator()

while True:
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text.lower() == "exit":
                break

            try:
                translated_text = translator.translate(speech_text, dest='fr').text
                print(translated_text)

                voice = gTTS(translated_text, lang='fr')
                voice.save("voice.mp3")
                playsound("voice.mp3")
                os.remove("voice.mp3")

            except Exception as translation_error:
                print(f"Translation error: {str(translation_error)}")

        except sr.UnknownValueError:
            print("Couldn't understand")
        except sr.RequestError as request_error:
            print(f"Couldn't request results from Google: {str(request_error)}")
