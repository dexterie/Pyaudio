import json
import speech_recognition as sr
from datetime import datetime

r = sr.Recognizer()
run = True
data = {}
with open("note.json", "r") as f:
    data = json.load(f)

while run:
    with sr.Microphone() as sound:
        print("Woking")
        audio_text = r.listen(sound)
        print("Done")
 
        try:
            text = r.recognize_google(audio_text)
            r.energy_threshold = 300
            print(json.dumps(data, indent= 4))


            now = datetime.now()
            data["note"].append ({
                str(now) : text
            })

            with open("note.json", "w") as output:
                output.write(json.dumps(data, indent= 4))
        
        except KeyboardInterrupt:
            print("Stop!")
        except:
            print("Error!")
            run = False