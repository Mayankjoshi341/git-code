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
recode_1 = {'Ꝉ': 'a', 'ꝉ': 'b', 'Ꝋ': 'c', 'ꝋ': 'd', 'Ꝍ': 'e', 'ꝍ': 'f', 'Ꝏ': 'g', 'ꝏ': 'h', 'Ꝑ': 'i',
    'ꝑ': 'j', 'Ꝓ': 'k', 'ꝓ': 'l', 'Ꝕ': 'm', 'ꝕ': 'n', 'Ꝗ': 'o', 'ꝗ': 'p', 'Ꝙ': 'q', 'ꝙ': 'r',
    'Ꝛ': 's', 'ꝛ': 't', 'Ꝝ': 'u', 'ꝝ': 'v', 'Ꝟ': 'w', 'ꝟ': 'x', 'Ꝡ': 'y', 'ꝡ': 'z', '^': ' ',
    '~': '.', '*': "'", '#': '!'}
recode_2 = {'Ꝿ': 'a', 'ꝿ': 'b', 'Ꞁ': 'c', 'ꞁ': 'd', 'Ꞃ': 'e', 'ꞃ': 'f', 'Ꞅ': 'g', 'ꞅ': 'h', 'Ꞇ': 'i',
    'ꞇ': 'j', 'ꞈ': 'k', '꞉': 'l', '꞊': 'm', 'Ꞌ': 'n', 'ꞌ': 'o', 'Ɥ': 'p', 'ꞎ': 'q', 'ꞏ': 'r',
    'Ꞑ': 's', 'ꞑ': 't', 'Ꞓ': 'u', 'ꞓ': 'v', 'ꞔ': 'w', 'ꞕ': 'x', 'Ꞗ': 'y', 'ꞗ': 'z', '^': ' ',
    '~': '.', '*': "'", '#': '!'
}
recode_3 = {'Ꝣ': 'a', 'ꝣ': 'b', 'Ꝥ': 'c', 'ꝥ': 'd', 'Ꝧ': 'e', 'ꝧ': 'f', 'Ꝩ': 'g', 'ꝩ': 'h', 'Ꝫ': 'i',
    'ꝫ': 'j', 'Ꝭ': 'k', 'ꝭ': 'l', 'Ꝯ': 'm', 'ꝯ': 'n', 'ꝰ': 'o', 'ꝱ': 'p', 'ꝲ': 'q', 'ꝴ': 'r',
    'ꝵ': 's', 'ꝷ': 't', 'ꝸ': 'u', 'ꝺ': 'v', 'Ꝼ': 'w', 'Ꝼ': 'x', 'ꝼ': 'y', 'Ᵹ': 'z', '^': ' ',
    '~': '.', '*': "'", '#': '!'
}
recode_4 = {'Ꞙ': 'a', 'ꞙ': 'b', 'Ꞛ': 'c', 'ꞛ': 'd', 'Ꞝ': 'e', 'ꞝ': 'f', 'Ꞟ': 'g', 'ꞟ': 'h', 'Ꞡ': 'i',
    'ꞡ': 'j', 'Ꞣ': 'k', 'ꞣ': 'l', 'Ꞥ': 'm', 'ꞥ': 'n', 'Ꞧ': 'o', 'ꞧ': 'p', 'Ꞩ': 'q', 'ꞩ': 'r',
    'Ɦ': 's', 'Ɜ': 't', 'Ɡ': 'u', 'Ɬ': 'v', 'Ɪ': 'w', 'ꞯ': 'x', 'Ʞ': 'y', 'Ʇ': 'z', '^': ' ',
    '~': '.', '*': "'", '#': '!'
}
recode_5 = {'Ʝ': 'a', 'Ꭓ': 'b', 'Ꞵ': 'c', 'ꞵ': 'd', 'Ꞷ': 'e', 'ꞷ': 'f', 'Ꞹ': 'g', 'ꞹ': 'h', 'Ꞻ': 'i',
    'ꞻ': 'j', 'Ꞽ': 'k', 'ꞽ': 'l', 'Ꞿ': 'm', 'ꞿ': 'n', 'Ꟁ': 'o', 'ꟁ': 'p', 'Ꟃ': 'q', 'ꟃ': 'r',
    'Ꞔ': 's', 'Ʂ': 't', 'Ᶎ': 'u', 'Ꟈ': 'v', 'ꟈ': 'w', 'Ꟊ': 'x', 'ꟊ': 'y', 'ā': 'z', '^': ' ',
    '~': '.', '*': "'", '#': '!'
}

code_select = (code_1 , code_2, code_3 , code_4 , code_5)
code = random.choice(code_select)
def msg():
    print("\n")
    print("______||ENTER THE FUNCTION FROM BELOW||______")
    print("______|1 For Encode||2 For Decode|____________")
    op = input("==>")
    match op:
        case "1":
            encode()
        case '2':
            decode()

def encode():
    typ = {"code_1" : "!*", "code_2" : "@&", "code_3" : "#^", "code_4" : "$%", "code_5" :"+-"}
    print("HELLO, WELLCOME TO THE ENCODER!")
    print("Please enter your secret massage") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(1)
    print("....")
    msg = [*text]
    i = 0
    print("Message converted successfully")
    print("Encoded message is :")
    while i < len(msg):
        time.sleep(0.3)
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
        exit()    
def decode():
    print("HELLO, WELLCOME TO THE DECODER!")
    print("Please enter your secret code") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(1)
    print("....")
    
    value_to_find = [*text]
    for_recode = value_to_find[:-2]
    first_code = value_to_find[:1]
    if first_code[0] in recode_1:
        final_dic = recode_1
    elif first_code[0] in recode_2:
        final_dic = recode_2
    elif first_code[0] in recode_3:
        final_dic = recode_3
    elif first_code[0] in recode_4:
        final_dic=recode_4  
    elif first_code in recode_5:
        final_dic = recode_5
    else:
        exit()
    print("Message converted successfully")
    print("Decoded message is :")
    i = 0 
    while i < len(value_to_find):
        time.sleep(0.3)
        s= final_dic[for_recode[i]]
        print(s, end = "")
        i += 1
        try:
           s= final_dic[for_recode[i]]
        except(IndexError):
            msg()
    print("\n")

while True:
       msg()
else:
    print(0)

match op:
        case "1":
            print("write 1 to decode ")
            int()
        case '2':
             print("write 1 to decode ")
             int()
  