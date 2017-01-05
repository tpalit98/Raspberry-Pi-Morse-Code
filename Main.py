#A project that uses the Raspberry Pi and a LED to display morse code


import time
import RPi.GPIO as GPIO

#Sets the numbering style of the GPIO pins
GPIO.setmode(GPIO.BOARD)
#Sets up the pin the LED will use
GPIO.setup(8,GPIO.OUT)

#Blink intervals in seconds
SHORT_BLINK = 0.3
LONG_BLINK = SHORT_BLINK*3

#Dictionary of letters, numbers, and characters that map to the corresponding morse code sequences
morse = {
    " ":"       ",
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "0":"-----",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    ".":".-.-.-",
    ",":"--..--",
    ":":"---...",
    "?":"..--..",
    "'":".----.",
    "-":"-....-",
    "/":"-..-.",
    "@":".--.-.",
    "=":"-...-"
}


#converts a character to morse code using the dictionary
#returns None if the character is not in the dictionary
def toMorse(c):
    if c in morse:

        return morse[c];

    else:

        return None;


#translates a morse code sequence into the appropriate blinks of the LED
def blink(str):
    length = len(str)
    #print(length)

    for j in range(0,length):

        c = str[j]

        if c == ".":
            
            GPIO.output(8,True)
            time.sleep(SHORT_BLINK)
            GPIO.output(8,False)
            time.sleep(SHORT_BLINK)
            #print("short")
        if c == "-":
            
            GPIO.output(8,True)
            time.sleep(LONG_BLINK)
            GPIO.output(8,False)
            time.sleep(SHORT_BLINK)
            #print("long")
        if c == " ":
            
            GPIO.output(8,False)
            time.sleep(SHORT_BLINK)
            #print("space")

    return;



while True:

    seq = input("Input a word including the letters A-Z and/or a number including the digits 0-9,"
                " or enter '~quit~ to exit': ")

    if seq == "~quit~":
        break


    length = len(seq)

    result = ""

    for i in range(0, length):
        c = seq[i]

        #converts input into uppercase
        if c.isalpha():
            c = c.upper()
        #checks for invalid characters
        if(toMorse(c) is None):
            print("Invalid character entered")
            result = "not a valid sequence"
            break


        result = result + toMorse(c) + "   "

    print("In morse code " + seq + " is " + result)

    blink(result)
    
    







