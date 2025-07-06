def count_words(text):
    words = text.split()
    n_words = len(words)
    return n_words

def count_chars(text):
    lower_text = text.lower()
    cnt_char = {}
    for char in lower_text:
        if char not in cnt_char:
            cnt_char[char] = 0
        cnt_char[char] += 1
    return cnt_char
