import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
#import os


# Creating Recogniser() class object
recog1 = spr.Recognizer()

# Creating microphone instance
mic = spr.Microphone() #device_index=0
	
# Translator method for translation
translator = Translator()

# srouce = english
from_lang = 'en'

# translated = hindi
to_lang = 'hi'

with mic as source:
	
	print("Speak a stentence...")
	recog1.adjust_for_ambient_noise(source, duration=0.5)
	
	# Storing the speech into audio variable
	audio = recog1.listen(source)

	# convert audio into text
	get_sentence = recog1.recognize_google(audio)
	try:
		
		# Printing Speech which need to
		# be translated.
		print("Phase to be Translated :"+ get_sentence)
		text_to_translate = translator.translate(get_sentence,
												src= from_lang,
												dest= to_lang)
		
		text = text_to_translate.text
		print(f"Translated text: {text}")
		speak = gTTS(text=text, lang=to_lang, slow= False)
		speak.save("captured_voice.mp3")
		playsound("captured_voice.mp3")
		

	except spr.UnknownValueError:
		print("Unable to Understand the Input")
	
	except spr.RequestError as e:
		print("Unable to provide Required Output".format(e))