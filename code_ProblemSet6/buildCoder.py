import string

#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    #shift
    dictionary = {}
    for e in string.ascii_uppercase: 
        dictionary[e]=chr((ord(e)-65+shift)%26+65)
    for e in string.ascii_lowercase:
        dictionary[e]=chr((ord(e)-97+shift)%26+97)
    return dictionary