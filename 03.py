sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 全ての文字を小文字に変換してから単語に分割
words = sentence.lower().split()

# 特殊文字(ここではピリオドとコンマ)を削除
words = [word.replace(".", "") for word in words]

# 各単語の文字数を計算してリストに保存
word_lengths = [len(word) for word in words]

print(word_lengths)
