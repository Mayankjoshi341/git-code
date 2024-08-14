import time
import numpy as np 
import string
code = {
    'a': '!',
    'b': '@',
    'c': '#',
    'd': '$',
    'e': '%',
    'f': '^',
    'g': '&',
    'h': '*',
    'i': '(',
    'j': ')',
    'k': '{',
    'l': '}',
    'm': '\\',
    'n': '"',
    'o': ';',
    'p': '<',
    'q': '>',
    'r': ',',
    's': '.',
    't': '?',
    'u': "'",
    'v': ':',
    'w': '+',
    'x': '-',
    'y': '_',
    'z': '~'
}

def commit():
    continuee = str(input())
    if continuee.lower() == 'y':
        main()
    else:
        print("goodbye folkes!")
        exit()

def main():
    """
    The main function prompts the user to choose between encoding or decoding and then calls the
    corresponding function based on the user's choice.
    """
    print('enter "encode" or "decode"')
    op = input("==>")
    match op:
        case 'encode':
            encode()
        case 'decode':
            decode()
def encode():
    print("hello folkes!")
    print("enter the text ") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(2)
    print("....")
    msg = [*text]
    length = len(msg) - 1
    while length != 0:
      s = code[msg[length]]
      print(s, end = "")
      if length == 0:
          break
      length= length - 1

def decode():
    print("hello folkes!")
    print("enter the text ") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(2)
    print("....")

while True:
       commit()