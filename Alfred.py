#!/usr/bin/python3
#Alfred

#Description:
#Insipred from the character Alfred J. Pennyworth from DC comics.
#Alfred is personal digital assistant who will help you in maintaing your personal and work life.

#Developed by: Kshithij Iyer
#Contact: ahole@disroot.org

#Date when project started:19/12/2017
#Last modification done on:2/1/2018

#Settings:
#General Settings:
#Specify your name. The name bu which you want to be refered to.
your_name="Kshithij"
#Specify if you want to be specified as Sir/Madam.
refer_me_as="Sir"
#The name of your personal digital assistant.
my_name="Alfred"
#The name of the city where you live.
city="Pune"

#Twitter Settings:
#consumer key for twitter app
consumer_key="nh3J5DPvhezSYwInlfWVwBvDU"
#consumer secret for twitter app
consumer_secret="1p3IPnfWaPZEKzTza4DKnNhW5jIF7udzgJf1Tj0ulOG5mLCxmB"
#access token for twitter app
access_token= "796761081389662209-oI135w0wnBAiGPtM56LQarHsmkcMEI9"
#access token secret for twitter app
access_token_secret="37aGYc8ZPoBiSI3RarMXqflR7FKsEEjdliX1Pf7EFMSXv"


#importing packages
from gtts import gTTS
from weather import Weather
import os, datetime, tweepy, random, wikipedia

#Getting current time 
currentTime = datetime.datetime.now()
#counter variable
counter=0
#Typical chat statements and their responces
lets_start=["let's talk","i am bored","let's chit chat","let's chat"]
start_phrases=["Let's talk!","Yes! Even I am bored as well.","Let's chit chat!","Let's have a nice conversation."]
greetings = ['hola', 'hello', 'hi','hey']
termination=["bye","goodbye","good bye","see you","tata","ta-ta","go to sleep","sleep","shutdown"]
shutdown_phrases=["Bye!","Goodbye!","Good bye!","See you soon!","tata!","I am going to sleep now!","I'll go crash."]
intro_phrases=["who are you?","introduce yourself","who the fuck are you?","wtf"]
twitter_phrases=["what's up on twitter?","twitter","what are my friends doing?","latest tweets","tweets","get tweets"]
weather_phrases=["should i go out?","what's the weather outside?","weather","how does the weather look?","is it hot or cold?","is it hot/cold?"]
time_phrases=["what's the time?","time please","tell me the time","may i know the time please","may i know the time","now","get time","time"]
weather_forecast_phrases=["get forecast","should I go for road trip?","should I travel?","is there a storm coming?","will it rain tomorrow?","what should I wear tomorrow?"]
twitter_trends_phrases=["get current trends","what's trending?","whatsup on twitter?","twitter trends","trending topics","current trends now","get trends"]
help_phrases=["How may I help you?","I am unable to understand what you want from me!","I don't have an answer for your question!","Sorry! I am not clear what you are asking me to do.","I can't do that!"]
suicide_detection_phrases=["i want to die","i want to kill myself","there is nothing left from me in this world","i want to quit","i quit"]
wiki_phrases=("search","who is","what is","tell me about","where is")

def about_me():
    "This function is there to introduce me where ever the user asks."
    text="Hello! I am "+my_name+". I am your digital assistant. I was developed by Kshithij Iyer. I am an open source software and my code is avaliable on github. I was developed and distrubuted under Apache 2.0 licence."
    say(text)
    text="I am always avaliable at your service."
    say(text)

def say(text):
    "A function to make Alfred say things."
    tts = gTTS(text, lang='en')
    tts.save("best.mp3")
    print(my_name+":"+text)
    os.system("mpg123 -q best.mp3")
    os.system("rm best.mp3")
    
def get_tweets():
    "This function gets first ten latest tweets tweeted by people who you follow on the Twitter."
    #Connecting to twitter using the credentials specified above.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    counter,users,who_all_tweeted,tweets=0,[],"",""
    for tweet in public_tweets:
        users.append(tweet.user.name)
        tweets=tweets+tweet.user.name+" : "+tweet.text+"\n"
        counter=counter+1
        if counter>10:
            for user in list(set(users)):
                who_all_tweeted=who_all_tweeted+user+", "
            who_all_tweeted=who_all_tweeted+"tweeted the following tweets on Twitter."
            break
    say(who_all_tweeted)
    print(tweets)

def get_trends():
    "This function gets current trend based on current location from twitter."
    say("I am displaying the top ten trending topics on twitter on your screen.")
    print("Trends:")
    #Connecting to twitter using the credentials specified above.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    all_cities= api.trends_available()
    counter=1
    for one_city in all_cities:
        if one_city['name']==city:
            trends=api.trends_place(one_city['woeid'])
            trends_collection = set([trend['name'] for trend in trends[0]['trends']])
            for trend in trends_collection:
                print(trend)
                if counter==10:
                    break
                counter=counter+1
            break
        
def post_tweet(tweet):
    "This function will be used to post status on twitter."
    #Connecting to twitter using the credentials specified above.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    status=api.update_status(status=tweet)
    say("Tweet successfully posted on twitter.")


def get_weather():
    "This function gets today's weather from Yahoo Weather XML RSS feed."
    weather = Weather()
    location = weather.lookup_by_location(city)
    forecasts = location.forecast()
    for forecast in forecasts:
        low=round((float(forecast.low())-32)/1.8,0)
        high=round((float(forecast.high())-32)/1.8,0)
        say("The weather outside is "+forecast.text()+". The maximum temperature is "+str(high).replace(".0","")+" degree celsius and the minimum temperature is "+str(low).replace(".0","")+" degrees celsius.")
        break

def get_weather_forecast():
    "This function gets the weather forcast from Yahoo Weather XML RSS feed."
    weather = Weather()
    location = weather.lookup_by_location(city)
    forecasts = location.forecast()
    say("Displaying the weather forecast on the screen.")
    for forecast in forecasts:
        low=round((float(forecast.low())-32)/1.8,0)
        high=round((float(forecast.high())-32)/1.8,0)
        print("Date:"+forecast.date()+" Weather:"+forecast.text()+" Max:"+str(high).replace(".0","")+" C Min:"+str(low).replace(".0","")+" C")
    
def get_time():
    "This function fetches time."
    now = datetime.datetime.now()
    say("Today is "+now.strftime("%A, %d %B %Y %I:%M%p")+".")

def prevent_suicide():
    "This is a user suicide prevention function."
    say("Think about your parents "+your_name+" . How would they feel when they'll see you dead?")
    say("Will they be proud of you?")
    say("Did they raise you for this day?")
    say("Forget about them, what would I do without you "+refer_me_as+"?")
    say("Suicide is not the way out "+refer_me_as+"! Stay strong! Everything will be fine. I am always there for you "+refer_me_as)

def get_wiki(word):
    "This function speaks out the wiki summary for a give word."
    try:
        wiki = wikipedia.summary(word)
        say(wiki)
    except wikipedia.exceptions.DisambiguationError as error:
        say("The word \""+word+" can mean a lot of things. Please be specific.")
        print(error.options)

while True:
    
    #initial Greeting settings 
    if currentTime.hour < 12:
        Greetings="Good morning "
    elif currentTime.hour < 18:
        Greetings="Good afternoon "
    else:
        Greetings="Good evening "
        
    if counter==0:
        text=Greetings+refer_me_as+"!"+" I am "+my_name+". Your digital assistant."
        say(text)
        get_weather()
        counter=counter+1
        text=refer_me_as+"! Should I run the commands file?"
        say(text)
        command=input("[Yes/No]:")
        if command.lower()=="yes" or command.lower()=="y" :
            text="Running commands!"
            say(text)
            commands_file=open("commands.txt")
            while True:
                command=commands_file.readline()
                if(command):
                     os.system(command)
                else:
                    commands_file.close()
                    break
            text="Done "+refer_me_as+"!"
            say(text)
        else:
            text="Okay! I'll do something else."
            say(text)
    command=input(your_name+":")
    command=command.replace("!","")
    command=command.replace(".","")
    command=command.lstrip()
    if command.lower() in lets_start:
        say(random.choice(start_phrases))
    elif command.lower() in greetings:
        say(random.choice(greetings))
    elif command.lower() in termination:
        say(random.choice(shutdown_phrases))
        break;
    elif command.lower() in intro_phrases:
        about_me()
    elif command.lower() in twitter_phrases:
        get_tweets()
    elif command.lower() in weather_phrases:
        get_weather()
    elif command.lower() in time_phrases:
        get_time()
    elif command.lower() in weather_forecast_phrases:
        get_weather_forecast()
    elif command.lower() in twitter_trends_phrases:
        get_trends()
    elif command.lower() in suicide_detection_phrases:
        prevent_suicide()
    elif command.lower().startswith(wiki_phrases):
        search_word=command.replace("?","")
        search_word=search_word.lower()
        for index in range(0,len(wiki_phrases)):
            search_word=search_word.replace(wiki_phrases[index],"")
        word=search_word.lstrip()
        get_wiki(word)
    elif command.lower().startswith("tweet:"):
        tweet=command.replace("Tweet:","").replace("tweet:","")
        tweet=tweet+" #ProjectAlfred"
        post_tweet(tweet)        
    else:
        say(random.choice(help_phrases))

    
