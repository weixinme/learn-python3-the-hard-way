def break_words(stuff):
    words = stuff.split(' ')
    return words


def sort_word(words):
    return sorted(words)


def print_first_word(words):
    word = words.pop(0)
    print(word)


def print_last_world(words):
    word = words.pop(-1)
    print(word)


def sort_sentence(setence):
    words = break_words(setence)
    return sort_word(words)


def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_world(words)


def print_fist_and_last_sorted(sentence):
    words = sort_word(sentence)
    print_first_word(words)
    print_last_world(words)
