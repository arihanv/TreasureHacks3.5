import speech_recognition as sr
import pyttsx3
import os
import pywhatkit
import datetime
import wikipedia
import pyjokes
import openai

import requests
from twilio.rest import Client
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

twilio_account_sid = 'personal key'
twilio_auth_token = 'personal key'
twilio_phone_number = '+1816 xxxxxx91'
twilio_client = Client(twilio_account_sid, twilio_auth_token)

ELEVENLABS_API_KEY="1ba0____personalkey______3720868670557"
ELEVANLABS_URL='https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM/stream'

openai.api_key = "sk-7e1PJEx6yEzj03zf____personalkey______te5MBwLqWE"
run = False

def talk(text):
    engine.say(text)
    engine.runAndWait()


def extract_command(phrase):
    # Convert phrase to lowercase
    phrase = phrase.lower()
    
    # Check if "sight" or "sense" is in the phrase
    if "sight" in phrase:
        # Remove everything before "sight"
        phrase = phrase.split("sight", 1)[1].strip()
    elif "sense" in phrase:
        # Remove everything before "sense"
        phrase = phrase.split("sense", 1)[1].strip()
    elif "site" in phrase:
        phrase = phrase.split("site", 1)[1].strip()
    elif "sight sense" in phrase:
        phrase = phrase.split("sight sense", 1)[1].strip()
    elif "side" in phrase:
        phrase = phrase.split("side", 1)[1].strip()



    else:
        take_command()
    
    # Return the extracted command
    return phrase

keywords = ['sight', 'sense', 'site', 'sight sense', 'side']
    # Do something


def take_command():
    command = ''  # set default value here
    try:
        with sr.Microphone() as source:
            print('listening...')
            #talk('Ask Me Anything!') ##MAY GET ANNOYING SO COMMENTED
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command) # Add this line to see what the command is
            print('sight' in command or 'sense' in command or 'site' in command or 'sight sense' in command) ##DETECTS IF THE COMMAND CONTAINS A TRIGGER WORD
        if any(keyword in command for keyword in keywords):
            run = True
            # Extract the command using the function we just made
            extracted_command = extract_command(command)
            if extracted_command:
                print(extracted_command)
                return extracted_command
            else:
                talk("Please Say That Again")
                take_commandBypass()

    except:
        command = ''

    if not command:
        return ''

    return take_command()


def take_commandBypass():
    command = ''  # set default value here
    try:
        with sr.Microphone() as source:
            print('listening...')
            #talk('Ask Me Anything!') ##MAY GET ANNOYING SO COMMENTED
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command) # Add this line to see what the command is
            return command

    except:
        command=''

def text_to_speech(text):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {ELEVENLABS_API_KEY}'}
    data = {'text': text, 'lang': 'en'}
    response = requests.post(f'{ELEVANLABS_URL}/v1/generate', headers=headers, data=json.dumps(data))
    if response.ok:
        audio_url = response.json()['data']['audio']
        os.system(f'start cmd /c vlc --play-and-exit "{audio_url}"')
    else:
        print(response.text)


def ask_openai(question):
    context = "the bot to work as an assistant. The bot is supposed to be very positive. The bot should give short but concise answers."
    prompt = f"{context} {question}\n"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      temperature=0.0, #low temperature for limited nonsense
      max_tokens=100
    )

    answer = response.choices[0].text.strip()
    return answer

def format_phone_number(phone_number):
    phone_number = phone_number.replace(" ", "").replace("-", "")
    if len(phone_number) == 10:
        formatted_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
        return formatted_number
    else:
        return None


def run_tejas():
    command = take_command()
    #print(command)
    if command == False:
        exit()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        try:
            response = requests.get("https://api.ampiri.com/v1/creatives/5bf8c5a5-f49a-449e-8cd5-15e0cb0e01f7")
            with open("song.mp3", "wb") as f:
                f.write(response.content)
            engine.setProperty('voice', voices[0].id)
            engine.say(f"Playing {song}")
            engine.runAndWait()
            engine.setProperty('voice', voices[1].id)
        except:
            talk("Sorry, I could not play the song.")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'creator' in command:
        talk('We created this for Treasurehacks 2023')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif any(word in command for word in ['shut', ' quit', ' mute', ' stop', ' done', ' end',' terminate']): #spaces needed so a word like "friend" wont trigger
        talk('Goodbye!')
        take_command()
    elif 'name' in command:
        talk("My name is Sight Sense.")
    elif 'text' in command or 'message' in command:
        # Prompt the user for the phone number and message content using voice input
        talk("Enter the phone number you want to send a text message to.")
        to_number = take_commandBypass()
        to_number = "+1" + to_number #ADD THE COUNTRY CODE

        # Format the phone number to match Twilio's requirements
        #to_number = format_phone_number(to_number)

        talk("Enter the message you want to send.")
        letter = take_commandBypass()

        # Set up the Twilio client with your account SID and auth token
        client = Client(twilio_account_sid, twilio_auth_token)

        # Use the client to send a text message with Twilio's API
        message = client.messages.create(
            body=letter,
            from_=twilio_phone_number,
            to=to_number
        )

        # Print out the message SID as confirmation that the text message was sent
        print(f"Message sent with SID: {message.sid}")
    elif 'call' in command:
        # Prompt the user for the phone number to call
        talk("Enter the phone number you want to call.")
        to_number = take_commandBypass()
        to_number = "+1" + to_number #ADD THE COUNTRY CODE

        client = Client(twilio_account_sid, twilio_auth_token)


        # Use the Twilio client to initiate a call with Twilio's API
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=to_number,
            from_=twilio_phone_number
        )

        # Print out the call SID as confirmation that the call was initiated
        print(f"Call initiated with SID: {call.sid}")
           
    else:
        try:
            response = openai.Completion.create(
              prompt=f"{command}\n",
              model="text-davinci-003",
              top_p=1,
              frequency_penalty=0.0,
              presence_penalty=0.0,
              temperature=0.0, #low temperature for limited nonsense
              max_tokens=100
            )
            answer = response.choices[0].text.strip()
            talk(answer)
            if '?' in answer: #IF THE BOT IS ASKING THE USER A QUESTION
                take_commandBypass() #ALLOWS FOR FLUENT CONVERSATION
        except Exception as e:
            print(e)
            talk('Please say the command again.')
            take_commandBypass()


while True:
    run_tejas()



### OLD PLAY SONG ###

#    if 'play' in command:
#       song = command.replace('play', '')
#        talk('playing ' + song)
#       pywhatkit.playonyt(song)


### OLD TEXT ###

# elif 'text' in command:
#         try:
#             words = command.split()
#             phone_number = words[1]
#             if phone_number.isnumeric():
#                 text_message = ' '.join(words[2:])
#                 message = twilio_client.messages.create(
#                     body=text_message,
#                     from_=twilio_phone_number,
#                     to=phone_number
#                 )
#                 talk(f"Text message sent to {phone_number}")
#             else:
#                 contact_name = phone_number
#                 phone_number = contacts.get(contact_name.lower())
#                 if phone_number:
#                     text_message = ' '.join(words[2:])
#                     message = twilio_client.messages.create(
#                         body=text_message,
#                         from_=twilio_phone_number,
#                         to=phone_number
#                     )
#                     talk(f"Text message sent to {contact_name}")
#                 else:
#                     talk(f"Sorry, I could not find {contact_name} in your contacts.")
#         except:
#             talk('Sorry, I could not send the text message.')     

##OLD TTS WITH ELEVANLABS VOICE###

# def text_to_speech(text, voice='eleven-US-KevinV3'):
#     headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {ELEVENLABS_API_KEY}'}
#     data = {'text': text, 'lang': 'en', 'voice': voice}
#     response = requests.post(f'{ELEVENLABS_URL}/v1/generate', headers=headers, data=json.dumps(data))
#     if response.ok:
#         audio_url = response.json()['data']['audio']
#         os.system(f'start cmd /c vlc --play-and-exit "{audio_url}"')
#     else:
#         print(response.text)

###OLD TALK FUNCTION WITH ELEVANLABS VOICE###

# def talk(text, voice='eleven-US-Rachel'):
#     headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {ELEVENLABS_API_KEY}'}
#     data = {'text': text, 'lang': 'en', 'voice': voice}
#     response = requests.post(f'{ELEVENLABS_URL}/v1/generate', headers=headers, data=json.dumps(data))
#     if response.ok:
#         audio_url = response.json()['data']['audio']
#         os.system(f'start cmd /c vlc --play-and-exit "{audio_url}"')
#     else:
#         print(response.text)

# talk("test", voice='eleven-US-Rachel')
