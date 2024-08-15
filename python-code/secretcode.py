import time
import numpy as np 
import string
code = {
    'a': '!','b': '@','c': '#','d': '$','e': '%','f': '^','g': '&','h': '*','i': '(','j': ')',
    'k': '{','l': '}','m': '^','n': '"','o': ';','p': '<','q': '>','r': ',','s': '.','t': '?',
    'u': "'",'v': ':','w': '+','x': '-','y': '_','z': '~',' ': '/','.': "`"
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
    i = 0
    while i < len(msg):
        time.sleep(0.5)
        s= code[msg[i]]
        print(s, end = "")
        i += 1
    print("\n")

def decode():
    print("hello folkes!")
    print("enter the text ") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(2)
    print("....")
    value_to_find = [*text]
    key = [key for key , value in code.items() if value in value_to_find]
    msg = ''.join(key)
    print(msg)

while True:
       main()