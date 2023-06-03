import openai
from gtts import gTTS
import playsound 
from time import sleep as sl 

#descarga las librerias importadas en la terminal antes de probar 
#pip install openai --- pip install gtts --- pip install playsound
intro = print('CHATGPT + AUDIO')
sl(2)
intro = print('create by Edwin')


openai.api_key = "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"
dato = input('escribe tu pregunta: ')
print('procesando...')

#prompt es donde colocas las preguntas:
ai = openai.Completion.create( engine='text-davinci-003',
                                     prompt= dato,
                                     max_tokens = 1000
                                      )


#se guarda la respuesta
respuesta = str(ai.choices[0].text)


tts = gTTS(respuesta, lang='es-us')

with open("wenas.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)

print("listo")
playsound.playsound('wenas.mp3')
