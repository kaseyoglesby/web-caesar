def alphabet_position(letter):
    return ord(letter.upper())-65


def rotate_character(char, rot):
    if not char.isalpha():
        return char
    neword = ((alphabet_position(char) + rot) % 26) + 65
    if char.islower():
        return chr(neword).lower()
    else:
        return chr(neword)
