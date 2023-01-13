def reverse_words(s):
    texts = s.split(' ')   
    reversed_texts = texts[::-1]
    return ' '.join(reversed_texts)
    