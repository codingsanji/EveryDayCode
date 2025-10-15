'''weird encrypter---
I read somewhere that if the first and last letter of a word is in the correct positions,
even if the rest of the word is jumbled, your brain automatically fills in the word for you.

Alex joked about how data isn't safe anywhere on Discord during ML&AI class so I started typing text
encrypted like what is described on top. I was significantly slow so decided to code this:

Program will run until escape is pressed. Every time you press enter it encrypts each word in your sentence
in the format below (and then is automatically copied when it gives output):
{(first letter)(backward order of the remaining middle letters) (last letter)}. '''


import keyboard
import pyperclip
import threading
import sys

stop_program = False

#escape check
def esc_listener():
    global stop_program
    keyboard.wait("esc")
    stop_program = True   
threading.Thread(target=esc_listener, daemon=True).start()

#encrypt word
def word_crypt(word):
    if len(word)<=3:
        return word
    else:
        first=word[0]
        last=word[-1]
        mid=word[1:-1]
        
        reversed_mid= ""
        for i in range(len(mid)-1 , -1, -1):
            reversed_mid+=mid[i]
        
        result=first+reversed_mid+last
        return result

#encrypt sentence
def line_crypt(line):
    words=line.split()
    crypt_words=[word_crypt(w) for w in words]
    
    final=""
    for word in crypt_words:
        final+=word+ " "
    final=final.strip()
    return final


print("Welcome to my weird encrypter!")
print("Keep typing typing and at the end of each sentence press enter to get the sentence encrypted.")
print("To exit program just press the ESC any time.")
print()

while True:
    if stop_program:   # check if ESC was pressed
        print("\nBye mate! It was fun playing with you.")
        sys.exit(0)
        
    line = input("Type your sentence: ")

    if stop_program:   # check if ESC was pressed
        print("\nBye mate! It was fun playing with you.")
        sys.exit(0)
        
    encrypted = line_crypt(line)
    pyperclip.copy(encrypted)   

    print("Encrypted line:", encrypted)
    print("(Copied to clipboard. Press ctrl+v to paste.)")
    print()
    

