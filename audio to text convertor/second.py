import speech_recognition as sr

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("kuch bol de bhai: ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("you said: " + text)

            # Save the recognized text to a file
            with open("audio.txt", "w") as file:
                file.write(text + "\n")

            print("Saved to audio.txt")

        except Exception as e:
            print("Error: " + str(e))

if __name__ == "__main__":
    main()
