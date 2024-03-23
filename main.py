import speech_recognition as sr
import pyttsx3

#initialize
r = sr.Recognizer()

def record_text():
    while(1):
        try:
            print("Speak something")
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic, duration=0.2)

                audio2 = r.listen(mic)

                Mytext = r.recognize_amazon(audio2)

                return Mytext
                 
                

        except sr.RequestError as e:
            print("folllowing error occured : {}".format(e))
        except sr.UnknownValueError:
            print("Unknown value error : {}")
    return

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return 

while 1:
    text = record_text()
    output_text(text)
    print("wrote text") 