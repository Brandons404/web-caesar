from helper import rotate_character


def encrypt(text, rot):
    new_text = ''
    for c in text:
        new_text += rotate_character(c,rot)
    return new_text
