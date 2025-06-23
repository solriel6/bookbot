def countwords(file_string):
    text_list = file_string.split()
    return len(text_list)

def countcharacters(file_string):
    all_lower_string = file_string.lower()
    letter_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        "æ": 0,
        "œ": 0,
        "ë": 0,
        "â": 0,
        "à": 0,
        "ê": 0,
        "é": 0,
        "è": 0,
        "ô": 0,
        "ח": 0,
        "ו": 0,
        "ϰ": 0,
        "η": 0,
        "τ": 0,
        "ο": 0,
        "ς": 0
    }
    for char in all_lower_string:
        if char.isalpha() == True:
            letter_count[char] += 1
        else:
            continue
    return letter_count

def sort_on(items):
    return items["num"]

def sort_characters(charactercount):
    sorted_characters = []
    for char in charactercount:
        mini_dictionary = {"char": char, "num": charactercount[char]}
        sorted_characters.append(mini_dictionary)
        sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters

