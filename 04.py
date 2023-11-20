# どうやらCode execution stateがresetされてしまったようです。もう一度コードを実行します。

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 単語に分解
words = sentence.split()

# 特殊文字を削除
words = [word.replace(".", "") for word in words]

# 1文字を取り出す単語の位置
one_char_positions = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# 連想配列を作成
elements = {}
for i, word in enumerate(words, start=1):
    if i in one_char_positions:
        elements[word[0]] = i
    else:
        elements[word[:2]] = i

print(elements)
