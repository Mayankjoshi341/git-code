import time
import numpy as np 
import string
import mysql.connector as connector

code = {
    'a': '!','b': '@','c': '#','d': '$','e': '%','f': '^','g': '&','h': '*','i': '(','j': ')',
    'k': '{','l': '}','m': '^','n': '"','o': ';','p': '<','q': '>','r': ',','s': '.','t': '?',
    'u': "'",'v': ':','w': '+','x': '-','y': '_','z': '~',' ': '/','.': "`"
    }
recode = {
    '!': 'a', '@': 'b', '#': 'c', '$': 'd', '%': 'e', '^': 'f', '&': 'g', 
    '*': 'h', '(': 'i', ')': 'j', '{': 'k', '}': 'l', '^': 'm', '"': 'n', 
    ';': 'o', '<': 'p', '>': 'q', ',': 'r', '.': 's', '?': 't', "'": 'u', 
    ':': 'v', '+': 'w', '-': 'x', '_': 'y', '~': 'z', '/': ' ', '`': '.'
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
    time.sleep(1)
    print("....")
    msg = [*text]
    i = 0
    while i < len(msg):
        s= code[msg[i]]
        print(s, end = "")
        i += 1
    print("\n")

def decode():
    print("hello folkes!")
    print("enter the text ") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(1)
    print("....")
    value_to_find = [*text]
    i = 0 
    while i < len(value_to_find):
        s= recode[value_to_find[i]]
        print(s, end = "")
        i += 1
        time.sleep(0.5)
    print("\n")

while True:
       main()