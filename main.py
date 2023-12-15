import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import openai
from config import apikey
import datetime
import os
import random
#todo: making desktop assistant to write in translated lang for me and save it in a file
#todo: for weathing asking --- use weather api  openweathermap
# todo: for news api , site it self is news api and ask for different topic news like space or kpop

chatStr = []  # Initialize chatStr as an empty list

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr.append({"role": "user", "content": f"jiliu: {query}\nJudy: "})  # Append the new message to chatStr

    while True:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chatStr,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Check if 'choices' field exists and if there are any choices
        if "choices" in response and response["choices"]:
            content = f"{response['choices'][0]['message']['content']}\n"
            chatStr.append({"role": "assistant", "content": content})  # Append the assistant's response to chatStr
            print(content)
            say(content)  # Speak the response by Judy

            # Check if user said "bye"
            if "bye".lower() in query.lower():
                # Save the entire chat conversation to a file
                say("yeah bye talk to you later")
                if not os.path.exists("Openai"):
                    os.mkdir("Openai")

                with open("Openai/chat_history.txt", "w") as f:
                    for message in chatStr:
                        f.write(f"{message['content']}\n")
                exit()
                break

            # Get user input for the next round of conversation
            query = takeCommand()
            chatStr.append({"role": "user", "content": f"jiliu: {query}\nJudy: "})

        else:
            print("No response content found.")
            break


    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # Extracting the relevant part of the message for file naming
    file_name_part = ' '.join(query.split('robot')[1:]).strip()

    # Ensure there is a valid file name part before creating the file
    if file_name_part:
        file_name = f"Openai/messages-{file_name_part}.txt"
    else:
        # If there is no valid file name part, use a random number
        file_name = f"Openai/messages-{random.randint(11, 34214234321)}.txt"

    with open(file_name, "w") as f:
        f.write(chatStr)

def ai(message):
    openai.api_key = apikey
    text = f"Openai response for Prompt: {message} \n *******************************\n\n"
    messages = [
        {"role": "user", "content": message}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Check if 'choices' field exists and if there are any choices
    if "choices" in response and response["choices"]:
        content = response["choices"][0]["message"]["content"]
        print(content)
        text += content
    else:
        print("No response content found.")

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # Extracting the relevant part of the message for file naming
    file_name_part = ' '.join(message.split('robot')[1:]).strip()

    # Ensure there is a valid file name part before creating the file
    if file_name_part:
        file_name = f"Openai/messages-{file_name_part}.txt"
    else:
        # If there is no valid file name part, use a random number
        file_name = f"Openai/messages-{random.randint(11, 34214234321)}.txt"

    with open(file_name, "w") as f:
        f.write(text)


#with pyttsx3 we can use say in windows too which was originally only for macbook
def say(text):
    #os.system(f"say{text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#this method will take the input from the mic
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6 removing it as by default it is 0.8
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. judy is apologetic "



if __name__ == '__main__':
    print('PyCharm')
    say("Judy here, how can i help you today ? ")
    #so that it will keep on listening
    while True:
        print("listening....")
        query = takeCommand()
        #say(query)
        sites = [["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"],["webtoon","https://www.webtoons.com/en/"],["spotify","https://open.spotify.com/?flow_ctx=1b1bd996-f1a9-4603-bbef-9e6b19cf7e94%3A1689887210"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"as your commands sailing to {site[0]} Captain...")
                webbrowser.open(site[1])

        if "Open gpt".lower() in query.lower():
            pathToGPT="https://chat.openai.com/"
            say("okay , here let's surf in gpt")
            webbrowser.open(pathToGPT)

        if "Open java".lower() in query.lower():
            eclipsePath = "C:/Users/Anjali Sharma/Desktop/Eclipse IDE.lnk"
            subprocess.Popen(["start", eclipsePath], shell=True)
            say("as the demands ... here's you ide")

        if "Open folder".lower() in query.lower():
            jiliufolderPath = "C:/Users/Anjali Sharma"
            subprocess.Popen(["explorer", jiliufolderPath], shell=True)
            say("roger that caption... here's the folder")

        if "the time".lower() in query.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Captain, the time right now is {current_time}")

        if "play mariposa".lower() in query.lower():
            tomariposa = "https://www.youtube.com/watch?v=U3RjdVmny6A"
            wayTomariposa ="https://wynk.in/music/song/mariposa/um_00842812123474-QZFZ21934119"
            say("here is the chorus !!!")
            webbrowser.open(tomariposa)

        moods = [["happy", "https://www.youtube.com/watch?v=U3RjdVmny6A"], ["sad", "https://www.youtube.com/watch?v=dS5GfL9F7L4"],
                 ["crazy", "https://www.youtube.com/watch?v=M6ZZKNPrSPw"], ["depressed", "https://www.youtube.com/watch?v=HQOQ52FkRzQ"],
                 ["melo", "https://www.youtube.com/watch?v=K-a8s8OLBSE"]]
        for mood in moods:
            if f"feeling {mood[0]}".lower() in query.lower():
                say(f"let's drive in {mood[0]} Captain...")
                webbrowser.open(mood[1])

        if "using robot".lower() in query.lower():
            say("wait for a while your content is being cooked")
            ai(message = query)

        if "have a chat".lower() in query.lower():
            print("Chatting......")
            say("hiiii master")
            chat(query)

        if "reset chat".lower() in query.lower():
            chartStr=""

        if " lets quit".lower() in query.lower():
            exit()

#todo: make a link or so so that it could open youtube and play the song i ask it to , rather than just depending on the emotion
#like in the sites , i can make it about emotions too right ... ilike i can have it play may favourite songs at my words , isn't it, like i start with the sites....
#todo:like folder, i can have it open camera

