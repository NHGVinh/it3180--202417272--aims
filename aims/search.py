
import unicodedata


def normalize_text(text):
    text = text.replace("\u0110", "D").replace("\u0111", "d")
    text = unicodedata.normalize("NFD", text)
    text = "".join(
        char for char in text
        if unicodedata.category(char) != "Mn"
    )
    return text.casefold()


def search_by_title(dvds, keyword):
    normalized_keyword = normalize_text(keyword)
    return [
        dvd for dvd in dvds
        if normalized_keyword in normalize_text(dvd.title)
    ]
