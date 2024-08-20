import time
import numpy as np 
import string
import random

code_1 = {'a': 'Ꝉ', 'b': 'ꝉ', 'c': 'Ꝋ', 'd': 'ꝋ', 'e': 'Ꝍ', 'f': 'ꝍ', 'g': 'Ꝏ', 'h': 'ꝏ', 'i': 'Ꝑ',
 'j': 'ꝑ', 'k': 'Ꝓ', 'l': 'ꝓ', 'm': 'Ꝕ', 'n': 'ꝕ', 'o': 'Ꝗ', 'p': 'ꝗ', 'q': 'Ꝙ', 'r': 'ꝙ',
 's': 'Ꝛ', 't': 'ꝛ', 'u': 'Ꝝ', 'v': 'ꝝ', 'w': 'Ꝟ', 'x': 'ꝟ', 'y': 'Ꝡ', 'z': 'ꝡ', ' ' : '^' , '.' :'~'
   , "'" : "*" , '!':'#'}
code_2 = {'a': 'Ꝿ', 'b': 'ꝿ', 'c': 'Ꞁ', 'd': 'ꞁ', 'e': 'Ꞃ', 'f': 'ꞃ', 'g': 'Ꞅ', 'h': 'ꞅ', 'i': 'Ꞇ',
 'j': 'ꞇ', 'k': 'ꞈ', 'l': '꞉', 'm': '꞊', 'n': 'Ꞌ', 'o': 'ꞌ', 'p': 'Ɥ', 'q': 'ꞎ', 'r': 'ꞏ',
 's': 'Ꞑ', 't': 'ꞑ', 'u': 'Ꞓ', 'v': 'ꞓ', 'w': 'ꞔ', 'x': 'ꞕ', 'y': 'Ꞗ', 'z': 'ꞗ', ' ' : '^' , '.' :'~' ,
   "'" : "*" , '!':'#'}
code_3 = {'a': 'Ꝣ', 'b': 'ꝣ', 'c': 'Ꝥ', 'd': 'ꝥ', 'e': 'Ꝧ', 'f': 'ꝧ', 'g': 'Ꝩ', 'h': 'ꝩ', 'i': 'Ꝫ',
 'j': 'ꝫ', 'k': 'Ꝭ', 'l': 'ꝭ', 'm': 'Ꝯ', 'n': 'ꝯ', 'o': 'ꝰ', 'p': 'ꝱ', 'q': 'ꝲ', 'r': 'ꝴ',
 's': 'ꝵ', 't': 'ꝷ', 'u': 'ꝸ', 'v': 'ꝺ', 'w': 'Ꝼ', 'x': 'Ꝼ', 'y': 'ꝼ', 'z': 'Ᵹ', ' ' : '^' , '.' :'~' ,
   "'" : "*" , '!':'#'}
code_4 = {'a': 'Ꞙ', 'b': 'ꞙ', 'c': 'Ꞛ', 'd': 'ꞛ', 'e': 'Ꞝ', 'f': 'ꞝ', 'g': 'Ꞟ', 'h': 'ꞟ', 'i': 'Ꞡ',
 'j': 'ꞡ', 'k': 'Ꞣ', 'l': 'ꞣ', 'm': 'Ꞥ', 'n': 'ꞥ', 'o': 'Ꞧ', 'p': 'ꞧ', 'q': 'Ꞩ', 'r': 'ꞩ',
 's': 'Ɦ', 't': 'Ɜ', 'u': 'Ɡ', 'v': 'Ɬ', 'w': 'Ɪ', 'x': 'ꞯ', 'y': 'Ʞ', 'z': 'Ʇ', ' ' : '^' , '.' :'~' ,
   "'" : "*" , '!':'#'}
code_5 = {'a': 'Ʝ', 'b': 'Ꭓ', 'c': 'Ꞵ', 'd': 'ꞵ', 'e': 'Ꞷ', 'f': 'ꞷ', 'g': 'Ꞹ', 'h': 'ꞹ', 'i': 'Ꞻ',
 'j': 'ꞻ', 'k': 'Ꞽ', 'l': 'ꞽ', 'm': 'Ꞿ', 'n': 'ꞿ', 'o': 'Ꟁ', 'p': 'ꟁ', 'q': 'Ꟃ', 'r': 'ꟃ',
 's': 'Ꞔ', 't': 'Ʂ', 'u': 'Ᶎ', 'v': 'Ꟈ', 'w': 'ꟈ', 'x': 'Ꟊ', 'y': 'ꟊ', 'z' : 'ā', ' ' : '^' , '.' :'~' ,
   "'" : "*" , '!':'#'} 


code_select = (code_1 , code_2, code_3 , code_4 , code_5)

code = random.choice(code_select)


recode = {
    '!': 'a', '@': 'b', '#': 'c', '$': 'd', '%': 'e', 'ṇ': 'f', '&': 'g', 
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
  
    print("enter 1 for encode and 2 for decode"
         )
    op = input("==>")
    match op:
        case "1":
            encode()
        case '2':
            decode()

typ = {"code_1" : "!*", "code_2" : "@&", "code_3" : "#^", "code_4" : "$%", "code_5" :"+-"}
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
    if code["a"] == 'Ꝉ':
        print(typ.get("code_1"))
    elif code["a"] == 'Ꝿ':
        print(typ.get("code_2"))
    elif code["a"] == 'Ꝣ':
        print(typ.get("code_3"))
    elif code["a"] == 'Ꞙ':
        print(typ.get("code_4"))
    elif code["a"] == 'Ʝ':
        print(typ.get("code_5"))
    else:
        commit()    
    print("\n")

def decode():
    print("hello folkes!")
    print("enter the text ") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(1)
    print("....")
    
    value_to_find = [*text]
    typ_code = value_to_find[-2:]
    print(typ_code)
    first_code = value_to_find[:1]
    print(first_code)
    if first_code in code_1:
        print(typ.get("code_1"))
    elif first_code in code_2:
        print(typ.get("code_2"))
    elif first_code in code_3:
        print(typ.get("code_3"))
    elif first_code in code_4:
        print(typ.get("code_4"))
    elif first_code in code_5:
        print(typ.get("code_5"))
    else:
        commit()
    i = 0 
    while i < len(value_to_find):
        time.sleep(0.5)
        s= recode[value_to_find[i]]
        print(s, end = "")
        i += 1
    print("\n")

while True:
       main()