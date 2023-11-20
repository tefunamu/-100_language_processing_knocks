text = "パタトクカシーー"

# Pythonのインデックスは0から始まるので1,3,5,7文字目はインデックス0,2,4,6
extracted_text = text[0] + text[2] + text[4] + text[6]

print(extracted_text)
