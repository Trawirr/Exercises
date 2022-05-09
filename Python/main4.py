def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join([str(alphabet.index(x)+1) for x in list(text.lower()) if x in alphabet])