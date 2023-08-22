import speech_recognition
import gtts 
import playsound
import os
import subprocess
import webbrowser
import datetime
import time
from plyer import notification
import psutil
import cv2
import wikipediaapi

class Assistant:
    once = 0
    ans = True
    def sound(self,aud):
        sound = gtts.gTTS(aud, lang="en")
        filename=("TEMP.mp3")
        sound.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.sound("Hello!, you have started Desktop assistant, what's your task ")
        print("Hello!, you have started Desktop assistant, what's your task ")
        self.Process()
     
    def Process(self):
            
            sentence = self.listen_user()
            sentence=sentence.lower()
            sentence=sentence.split()
            if sentence == None:
                self.sound("Something went wrong")
                exit()
            task = None
            website = self.website_checker(sentence)
            app = self.app_checker(sentence)

            if app != None or website != None:    
                task = self.task_checker(sentence)
            else:
                quit
            
            #print(task,website,app)

            #opens website
            if app == None and (task == "open" or website != None and task != "close"):
                    self.sound("opening "+website)
                    print("opening "+website)
                    url = f"https://www.{website}"
                    webbrowser.open(url)
                    
            #tells current time        
            elif "time" in sentence:
                current_time = datetime.datetime.now()
                formatted_time = current_time.strftime("%H:%M:%S")
                print("Formatted time:", str(formatted_time))
                self.sound("Now the time is"+formatted_time)
            

            #plays song
            elif "play" in sentence:
                song_name=sentence[1:]
                url = f"https://open.spotify.com/search/{song_name}"
                webbrowser.open(url)
            

            #opens internal app
            elif task == "open" and website == None and app != None:
                if app == 1:
                    self.open_camera()
                if app == 2:
                    self.open_settings()
                if app== 3:
                    subprocess.Popen("explorer /select,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
                if app == 4:
                    self.open_notepad()
                if app==5:
                    self.open_controlPanel()
   
            #close internal app
            elif task == "close" and website == None and app != None:
                if app == 1:
                    self.sound("closing camera")
                    cv2.destroyAllWindows()
                if app == 2:
                    self.sound("closing settings")
                    self.close_settings()
                #if app== 3:
                    #self.subprocess.Popen("explorer /select,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
                if app == 4:
                    self.sound("closing notepad")
                    self.close_notepad()
                #if app==5:
                    #self.open_controlPanel()

            #set remainder
            elif "reminder" in sentence:
                self.sound("after how many minutes do you want to get reminder")
                timeforremainder=int(self.listen_user())
                self.set_reminder(timeforremainder)      

            #Search Object
            elif "search" in sentence:
                # Specify a user agent for your application
                user_agent = "YourAppName/1.0 (YourContactInfo)"
                wiki_wiki = wikipediaapi.Wikipedia(
                    language='en',  # Language code for English Wikipedia, adjust as needed
                    user_agent=user_agent
                )
                page_title = [item for item in sentence if item != "search"]
                page = wiki_wiki.page(page_title)
                print(page_title)
                if page.exists():
                    print("Page title: ", page.title)
                    print("Page summary: ", page.summary)
                    self.sound("From wikipedia.com i found "+page.summary)
                else:
                    print("Could not find information")

            #default
            else:
                print("I don't know that")
                self.sound("OPPS!")

    def listen_user(self):
        if self.once < 2:
            with speech_recognition.Microphone() as source:

                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source) 
                try:
                    text = self.recognizer.recognize_google(audio)
                    print(f"you said: " + text)

                except Exception as e:
                    self.once += self.once
                    self.sound("I am sorry i didnt hear that, Can you repeat..")
                    text=self.listen_user()
                print('done listening')
                self.once = False
            return text

    def set_reminder(self,minutes):
        self.sound("What's the reminder for...")   
        notification_title = self.listen_user()
        self.sound("Ok reminder set after "+str(minutes)+" minutes to "+notification_title)
        time.sleep(minutes * 60)
        notification_message = "Reminder to "+notification_title
        notification_timeout = 10  # Notification will automatically close after 10 seconds
        notification.notify(
            title=notification_title,
            message=notification_message,
            timeout=notification_timeout
        )
        self.sound("You have A reminder of"+notification_title)

    def open_settings(self):
        try:
            os.system("start ms-settings:")
        except Exception as e:
            print(f"Error: {e}")

    def close_settings(self):
        try:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] == 'SystemSettings.exe':
                    psutil.Process(process.info['pid']).terminate()
                    print("Settings app closed successfully.")
                    return

            print("Settings process not found.")
        except Exception as e:
            print(f"Error: {e}")

    def open_camera(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Unable to access the camera.")
            return

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error: Failed to grab a frame.")
                break

            cv2.imshow("Camera", frame)

            # Add another way to close the camera window, for example, press 'ESC' key
            key = cv2.waitKey(1)
            if key == 27:  #27 is the ASCII value for 'ESC' key
                break

        cap.release()
        cv2.destroyAllWindows()

    def open_controlPanel(self):
        try:
            # Replace "control" with the appropriate command to open settings based on your OS.
            # On Windows, "control" opens the Control Panel.
            subprocess.run(["control"], shell=True)

        except subprocess.CalledProcessError as e:
            print("Error:", e)

    def open_notepad(self):
        try:
            subprocess.Popen("notepad.exe")
        except Exception as e:
            print(f"Error: {e}")

    def close_notepad():
        try:
            os.system("taskkill /IM notepad.exe /F")
        except Exception as e:
            print(f"Error: {e}")
  
    def task_checker(self,str):
        if "close" in str:
            return "close"
        else:
            return "open"

    def website_checker(self,str1):
        ret = None
        for i in range (str1.__len__()): 
            if str1[i].endswith('.com'):
                ret = str1[i]
        return ret

    def app_checker(self,str):
        if "camera" in str:
            return 1
        if "setting" in str or "settings" in str:
            return 2
        if "files" in str:
            return 3
        if "notes" in str:
            return 4
        if "control panel" in str:
            return 5
        else:
            return None
        
Assistant()