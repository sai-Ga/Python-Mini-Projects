import pyttsx3

text_converter = pyttsx3.init()
text = input("Enter text to convert  ")
text_converter.say(text)
text_converter.runAndWait() 