from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def listen_command():
    r = sr.Recognizer() #создаем новый объект
    with sr.Microphone() as source: #с помощью микрофона как источника
        print("Скажите вашу команду:")
        audio = r.listen(source) # считываем в аудио объект то, что произнесем


    try:
        our_speech = r.recognize_google(audio, language="ru") #возвращаем в виде текста
        print("Вы сказали: "+ our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError as e:
        return "ошибка"

   #return input("Скажите вашу команду:")

def do_this_command(message):
    message = message.lower() #ввод в нижнем регистре
    if "привет" in message:
        say_message("Привет друг!")
    elif "пока" in message:
        say_message("Пока!")
        exit()
    else:
        say_message("Команда не распознана!")

def say_message(message):
    voice = gTTS(message, lang = "ru") # запишем сообщение в переменную и получим mp3 файл на русском языке
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3" #рандомное имя файла
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("Голосовой ассистент: "+ message)

if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)


