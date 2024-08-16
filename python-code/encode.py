import string
import time 
import random
code = ("Ꝉ", "ꝉ", "Ꝋ", "ꝋ", "Ꝍ", "ꝍ", "Ꝏ", "ꝏ", "Ꝑ", "ꝑ", "Ꝓ", "ꝓ", "Ꝕ",
        "ꝕ", "Ꝗ", "ꝗ", "Ꝙ", "ꝙ", "Ꝛ", "ꝛ", "Ꝝ", "ꝝ", "Ꝟ", "ꝟ", "Ꝡ", "ꝡ",
        "Ꝣ", "ꝣ", "Ꝥ", "ꝥ", "Ꝧ", "ꝧ", "Ꝩ", "ꝩ", "Ꝫ", "ꝫ", "Ꝭ", "ꝭ", "Ꝯ", "ꝯ",
          "ꝰ", "ꝱ", "ꝲ", "ꝴ", "ꝵ", "ꝷ", "ꝸ", "ꝺ", "Ꝼ", "Ꝼ", "ꝼ", "Ᵹ", "Ꝿ", "ꝿ",
            "Ꞁ", "ꞁ", "Ꞃ", "ꞃ", "Ꞅ", "ꞅ", "Ꞇ", "ꞇ", "ꞈ", "꞉", "꞊", "Ꞌ", "ꞌ",
              "Ɥ", "ꞎ", "ꞏ", "Ꞑ", "ꞑ", "Ꞓ", "ꞓ", "ꞔ", "ꞕ", "Ꞗ", "ꞗ", "Ꞙ", "ꞙ",
                "Ꞛ", "ꞛ", "Ꞝ", "ꞝ", "Ꞟ", "ꞟ", "Ꞡ", "ꞡ", "Ꞣ", "ꞣ", "Ꞥ", "ꞥ", "Ꞧ",
                  "ꞧ", "Ꞩ", "ꞩ", "Ɦ", "Ɜ", "Ɡ", "Ɬ", "Ɪ", "ꞯ", "Ʞ", "Ʇ", "Ʝ", "Ꭓ",
                    "Ꞵ", "ꞵ", "Ꞷ", "ꞷ", "Ꞹ", "ꞹ", "Ꞻ", "ꞻ", "Ꞽ", "ꞽ", "Ꞿ", "ꞿ", "Ꟁ",
                      "ꟁ", "Ꟃ", "ꟃ", "Ꞔ", "Ʂ", "Ᶎ", "Ꟈ", "ꟈ", "Ꟊ", "ꟊ"
)
def encode():
    print("hello folkes!")
    print("enter the text ") 
    text = str(input("==>"))
    print("processing...")
    time.sleep(1)
    print("....")
    msg = [*text]
    for x in range(len(msg)):
        print(random.choice(code), end = "")
    print("\n")


def create_dis(code, msg):
    encoding_dis = {}
    decoding_dis = {}
    for chr in msg:
        random_symbol = random.choice(code)
        encoding_dis[chr] = random_symbol
        decoding_dis[random_symbol] = chr
        code.remove(random_symbol)
    return encoding_dis, decoding_dis
character = "abcdefghijklmnopqrstuvwxyzABCDEFGQRSTUVWXYZ0123456789 .,'"
def encode(encoding_dis,msg):
    return ''.join(encoding_dis[char] for char in msg)


while True:
    encode()    