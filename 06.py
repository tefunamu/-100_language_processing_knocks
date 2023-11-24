def bigram(words):
    return set(words[i:i+2] for i in range(len(words) - 1))

# Define the words
word1 = "paraparaparadise"
word2 = "paragraph"

# Create bi-grams
X = bigram(word1)
Y = bigram(word2)

# Compute the union, intersection, and difference
union = X | Y
intersection = X & Y
difference = X - Y

# Check for 'se' in X and Y
se_in_X = 'se' in X
se_in_Y = 'se' in Y

print(X, Y, union, intersection, difference, se_in_X, se_in_Y)


