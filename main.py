# I have to make a morse program it's a simple translate program I think.
# I m begining to search the table translate on wikipedia

# dictionary
international_morse_code = {
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
    " ":"       "
}

def morse_translator():
    key_list = list(international_morse_code.keys())
    translate = ""
    message = input("enter your message:\n").upper()
    for letter in message:
        for i in range(len(key_list)):
            if letter == key_list[i]:
                if international_morse_code[letter]:
                    translate += international_morse_code[letter]
    print(translate)


morse_translator()
