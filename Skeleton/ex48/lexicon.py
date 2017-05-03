directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat', 'open')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')


def get_tuple(word):
    lower_case = word.lower()

    if lower_case in directions:
        return 'direction', lower_case
    elif lower_case in verbs:
        return 'verb', lower_case
    elif lower_case in stop_words:
        return 'stop', lower_case
    elif lower_case in nouns:
        return 'noun', lower_case
    elif lower_case.isdigit():
        return 'number', int(lower_case)
    else:
        return 'error', word


def scan(sentence):
    words = sentence.split()
    return [get_tuple(word) for word in words]
