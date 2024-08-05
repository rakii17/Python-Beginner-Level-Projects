import pyttsx3

words = {
    "Me" : "Naanu", 
    "You" : "Neenu",
    "How" : "Hege",
    "From" : "Uru",
    "Give" : "Kodi",
    "Take" : "Tagoli",
    "Help" : "Sahaya",
    "Do" : "Maadi",
    "Ask" : "Keli"
}

words1 = {
    "Naanu" : "Me",
    "Neenu" : "You",
    "Hege" : "How",
    "Uru" : "Native/From",
    "Kodi" : "Give",
    "Tagoli" : "Take",
    "Sahaya" : "Help",
    "Maadi" : "Do",
    "Keli" : "Ask"
}


word = input("Enter the word you want to know the Kannada meaning : ")
# word = input("Enter the word you want to know the English meaning : ")

print(words.get(word))
# print(words1.get(word)) #For English Meaning

engine = pyttsx3.init()

engine.say(words.get(word))
# engine.say(words1.get(word))
engine.runAndWait()
