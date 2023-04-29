#Twillio API is REQUIRED for text/call
#GPT API is REQUIRED for generative AI (for when the bot doesn't know the answer)

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

twilio_account_sid = 'AC4cfec86d87d0f34359e07784172a6147'
twilio_auth_token = '46563c89b6315d38f74857fd9d8e6d72'
twilio_phone_number = '+18557432591'
twilio_client = Client(twilio_account_sid, twilio_auth_token)



openai.api_key = "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"


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''  # set default value here
    try:
        with sr.Microphone() as source:
            print('listening...')
            #talk('Ask Me Anything!') ##MAY GET ANNOYING SO COMMENTED
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tejas' in command:
                command = command.replace('tejas', '')
                print(command)
    except:
        pass
    return command


def text_to_speech(text):
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {ELEVENLABS_API_KEY}'}
    data = {'text': text, 'lang': 'en'}
    response = requests.post(f'{ELEVENLABS_URL}/v1/generate', headers=headers, data=json.dumps(data))
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
    print(command)
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
        talk('Tejas created this for Treasurehacks 2023')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('Goodbye!')
        quit()
    elif any(word in command for word in ['name', 'quit', 'mute', 'stop', 'done', 'end', 'terminate']):
        talk("My name is Sight Sense.")
    elif 'text' in command:
        # Prompt the user for the phone number and message content using voice input
        talk("Enter the phone number you want to send a text message to.")
        to_number = take_command()
        to_number = "+1" + to_number #ADD THE COUNTRY CODE

        # Format the phone number to match Twilio's requirements
        #to_number = format_phone_number(to_number)

        talk("Enter the message you want to send.")
        letter = take_command()

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
        except Exception as e:
            print(e)
            talk('Please say the command again.')
            run_tejas()


while True:
    run_tejas()



#    if 'play' in command:
#       song = command.replace('play', '')
#        talk('playing ' + song)
#       pywhatkit.playonyt(song)



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