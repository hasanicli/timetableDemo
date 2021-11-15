turkish_letters = {"ğ": "Ğ", "ü": "Ü", "ş": "Ş", "i": "İ", "ö": "Ö", "ç": "Ç", "ı": "I"}


def tr_title(text: str):
    new_texts = []
    old_texts = text.split()
    for txt in old_texts:
        for key, value in turkish_letters.items():
            txt = txt[0].replace(key, value) + txt[1:].replace(value, key)
        new_texts.append(txt.title())
    return " ".join(new_texts)
