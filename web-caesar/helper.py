
def alphabet_position(letter):
    up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_alpha = 'abcdefghijklmnopqrstuvwxyz'
    if letter.isupper():
        return up_alpha.index(letter)
    elif letter.islower():
        return low_alpha.index(letter)



def rotate_character(char, rot):
    new_char =''
    up_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_alpha = 'abcdefghijklmnopqrstuvwxyz'
    if char.isalpha():
      if char.isupper():
        index = alphabet_position(char)
        new_char = up_alpha[(index+rot) % 26]
        return new_char
      if char.islower():
        index = alphabet_position(char)
        new_char = low_alpha[(index+rot) % 26]
        return new_char
    else:
        new_char = char
        return char
