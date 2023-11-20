def ngram(n, sequence):
    """
    Function to create n-grams from a given sequence.
    Parameters:
    - n: integer, number of elements in each n-gram.
    - sequence: string or list, the sequence to break down into n-grams.
    Returns:
    - list of n-grams.
    """
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

sentence = "I am an NLPer"

# 文字bi-gram
char_bigrams = ngram(2, sentence)

# 単語bi-gram - 単語に分解してからngram関数に適用
word_bigrams = ngram(2, sentence.split())

print(char_bigrams, word_bigrams)
