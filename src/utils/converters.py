def convert_cyrillic_to_latin(text):
    cyrillic_to_latin = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "j",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "x",
        "ц": "s",
        "ч": "ch",
        "ш": "sh",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
        "ғ": "gʻ",
        "қ": "q",
        "ҳ": "h",
        "ў": "oʻ",
    }

    latin_text = ""
    for char in text.lower():
        if char in cyrillic_to_latin:
            latin_text += cyrillic_to_latin[char]
        else:
            latin_text += char
    return latin_text


def convert_latin_to_cyrillic(text):
    latin_to_cyrillic = {
        "a": "а",
        "b": "б",
        "v": "в",
        "g": "г",
        "d": "д",
        "e": "е",
        "yo": "ё",
        "j": "ж",
        "z": "з",
        "i": "и",
        "y": "й",
        "k": "к",
        "l": "л",
        "m": "м",
        "n": "н",
        "o": "о",
        "p": "п",
        "r": "р",
        "s": "с",
        "t": "т",
        "u": "у",
        "f": "ф",
        "x": "х",
        "ch": "ч",
        "sh": "ш",
        "ъ": "",
        "y": "ы",
        "": "ь",
        "e": "э",
        "yu": "ю",
        "ya": "я",
        "gʻ": "ғ",
        "q": "қ",
        "h": "ҳ",
        "oʻ": "ў",
        "o'": "ў",
    }

    cyrillic_text = ""
    latin_parts = text.split()
    for part in latin_parts:
        if part in latin_to_cyrillic:
            cyrillic_text += latin_to_cyrillic[part]
        else:
            cyrillic_text += part
        cyrillic_text += " "  # добавляем пробел между словами

    return cyrillic_text.strip()
