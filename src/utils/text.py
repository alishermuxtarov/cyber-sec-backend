import re


def clean_text(text):
    return re.sub(r"[^0-9a-zA-Zа-яА-Я,\-`'ўқғҳЎҚҒҲ\s]+", "", text)


def is_cyrillic(text):
    return any(ord(char) > 127 for char in text)
