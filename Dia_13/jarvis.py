import pathlib
import pyttsx3
import speech_recognition as sr
import pywhatkit 
import yfinance as yf 
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver el audio en texto 
def transformar_audio_en_texto():

    # almacenar el audio en una variable
    r = sr.Recognizer()

    #configurar el microfono 
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8 

        #informar el comienzo de la grabacion 
        print('Ya puedes hablar')

        #guardar lo que escuhe como audio
        audio = t.listen(origen)

        try:
            #buscar en google 
            pedido = r.recognize_google(audio, language='es-ar')

            #prueba de que pudo ingresar 
            print('Dijiste ' + pedido)

            #devolver pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print('Ups, no entendi lo que me dijiste')

            #devolver error 
            return 'Sigo esperando'

        #en caso de no resolver lo pedido
        except sr.RequestError:

            #prueba de que no compredio el audio 
            print('Ups, esperando...')

            #devolver error
            return 'Sigo esperando...'

        #error inesperado 
        except:
            #prueba de que no comprendio el audio 
            print('No te entiendo nada')

            #devovler error 
            return 'sigo esperando'

transformar_audio_en_texto()