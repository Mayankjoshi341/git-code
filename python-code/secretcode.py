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


def main():
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
    text = str(input("==>")).split()
    print("processing...")
    time.sleep(2)
    print("....")
    print(text[:2])
    print(code)
    


def decode():
    print("hello folkes!")
    print("enter the text ") 
    text = str(input("==>")).split(" ")
    print("processing...")
    time.sleep(2)
    print("....")
    print(text)


while True:
    main()