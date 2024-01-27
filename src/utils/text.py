import re


def clean_text(text):
    cleaned_text = re.sub(r"[^a-zA-Zа-яА-Я0-9\s]", "", text)
    return cleaned_text


def is_cyrillic(text):
    return any(ord(char) > 127 for char in text)
