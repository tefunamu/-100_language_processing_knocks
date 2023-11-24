import random

def Typoglycemia(msg):
    words = msg.split(' ')
    random_msg = ""
    for txt in words:
        if len(txt) > 4:
            shuffled_txt = txt[0] + "".join(random.sample(list(txt[1:-1]), len(txt)-2)) + txt[-1]
            random_msg += shuffled_txt + " "
        else:
            random_msg += txt + " "
    return random_msg.strip()  # 最後の余分なスペースを削除し、修正されたメッセージを返す

print(Typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"))
