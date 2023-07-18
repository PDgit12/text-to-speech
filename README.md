# text-to-speech


import pyttsx3
# print("welcome to robo speaker ")
if __name__ == "__main__":
    print("welcome to robo speaker")
    while True:
        x = input("enter what you want me to pronounce? or press q for quit: ")
        if x.upper() == "Q" or x.lower() == "q":
            command = pyttsx3.init()
            command.say("'Bye friend'")
            command.runAndWait()
            break
        
        command = pyttsx3.init()
        command.say(x)
        command.runAndWait() 
        rate = command.getProperty('rate')  # Get the current speaking rate
        new_rate = rate - 5 # Decrease the rate by 20 (adjust this value as needed)
        command.setProperty('rate', new_rate)
