def order_by(dict_item):
    # TODO: dict{"letter": "a", "count": 25}
    return dict_item["num"]

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

def sort_chars(char_dict):
    char_list = []
    for key in char_dict:
        char_num_dict = {}
        if key.isalpha():
            char_num_dict["char"] = key
            char_num_dict["num"] = char_dict[key]
        else:
            continue
        char_list.append(char_num_dict)
    char_list.sort(reverse=True, key=order_by)
    return char_list

