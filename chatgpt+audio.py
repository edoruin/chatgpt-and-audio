import openai
from gtts import gTTS
import playsound 
from time import sleep as sl 

#dowloand the librerys after run the code: 
#pip install openai --- pip install gtts --- pip install playsound
intro = print('CHATGPT + AUDIO')
sl(2)
intro = print('create by Edwin')


openai.api_key = " " #add one api_key of one openai account 
dato = input('escribe tu pregunta: ')
print('procesando...')

#prompt is for write the cuestions:
ai = openai.Completion.create( engine='text-davinci-003',
                                     prompt= dato,
                                     max_tokens = 1000
                                      )


#save the answer:
respuesta = str(ai.choices[0].text)


tts = gTTS(respuesta, lang='es-us')

with open("wenas.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)

print("listo")
playsound.playsound('wenas.mp3')
