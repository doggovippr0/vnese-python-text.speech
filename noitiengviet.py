from os import name
import os
import playsound
import wikipedia
import re 
import webbrowser
import smtplib
import requests
import urllib
from time import strftime
import pyaudio 
import pyttsx3
import speech_recognition as sr
import datetime
from gtts import gTTS
language = 'vi'
wikipedia.set_lang('vi')
engine = pyttsx3.init()
vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
engine.setProperty("voice",vi_voice_id)
now = datetime.datetime.now()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=5)
        try:
            yourvoice = r.recognize_google(audio, language="vi-VN")
            return yourvoice
        except:
            print("...")
            return get_audio()
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop()
    return 0
def speak(text):
    print("Bot: {}".format(text))
    engine.say(text)
    engine.runAndWait()
def open_application(text):
    if "word" in text:
        speak("Mở Microsoft Word")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile('C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        print("Chào buổi sáng {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        print("Chào buổi chiều {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        print("Chào buổi tối {}. Bạn đã ăn tối chưa nhỉ.".format(name))
# obtain audio from the microphone
print("Tôi có thể gọi bạn là gì?")
engine.say("Tôi có thể gọi bạn là gì?")
engine.runAndWait()
name = get_audio()
hello(name)
engine.say("Xin chào " +str(name))
engine.runAndWait()
while True:
    print("Robot: Tôi có thể giúp gì cho bạn không?")
    engine.say("Tôi có thể giúp gì cho bạn không?")
    engine.runAndWait()
    # recognize speech using Google Speech Recognition   
    yourvoice = get_audio()
    print("Tôi: " + yourvoice)        
    if "giờ" in yourvoice:
        brain = now.strftime("%H:%M:%S")
        print ("Robot: Xin chào "+str(name)+", Bây giờ đang là: " + str(brain))
        engine.say(brain)
        engine.runAndWait()
    elif "ngày" in yourvoice:
        brain = now.strftime("ngày %d tháng %m năm %Y")
        print("Robot: Xin chào "+str(name)+", Hôm nay là: "+brain)
        engine.say("xin chào, hôm nay là " +brain)
        engine.runAndWait()
    elif "tạm biệt" in yourvoice or "thôi" in yourvoice or "kết thúc" in yourvoice:
        brain = "Tạm biệt " + str(name) + ". Tôi sẽ tắt ngay thôi!"
        print(brain)
        engine.say(brain)
        engine.runAndWait()
        break
    elif "cu" in yourvoice:
        engine.say("Địt mẹ mày chửi thề với bố mày à! Cút!")
        engine.runAndWait()
        break
    elif "hãy chỉ" in yourvoice or "cho tôi biết" in yourvoice:
        tell_me_about()
    else: 
        print("Robot: Tôi không hiểu bạn đang nói gì! Xin hãy lặp lại!")
        engine.say("Tôi không hiểu bạn đang nói gì. Xin hãy lặp lại")
        engine.runAndWait()


    
