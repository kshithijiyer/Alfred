#Alfred

#Description:
#Insipred from the character Alfred J. Pennyworth from DC comics.
#Alfred is personal digital assistant who will help you help you in maintaing your personal and work life.

#Settings
#Specify if you want to be specified as Sir/Madam.
refer_me_as="Sir"
#The name of your personal digital assistant.
my_name="Alfred"

#importing packages
from gtts import gTTS
import os
import datetime


#Getting current time 
currentTime = datetime.datetime.now()
#counter variable
counter=0


while True:
    
    #initial Greetings 
    if currentTime.hour < 12:
        Greetings="Good morning "
    elif currentTime.hour < 18:
        Greetings="Good afternoon "
    else:
        Greetings="Good evening "
    if counter==0:
        text=Greetings+refer_me_as+"!"+" I am "+my_name+". Your personal digital assistant."
        print(text)
        tts = gTTS(text, lang='en')
        tts.save("good.mp3")
        os.system("mpg123 -q good.mp3")
        os.system("rm good.mp3")
        counter=counter+1

    #Awaiting commands 
    text="How may I help you?"
    tts = gTTS(text, lang='en')
    tts.save("good.mp3")
    os.system("mpg123 -q good.mp3")
    os.system("rm good.mp3")
    print(text)
    command=str(input(">"))
        
    #running things through command terminal
    if command.lower()=="" or command.lower()=="run command":
        tts = gTTS("Which command you want me to execute?", lang='en')
        tts.save("good.mp3")
        os.system("mpg123 -q good.mp3")
        os.system("rm good.mp3")
        
