import string

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    encryptedText = ''
    for letter in text:
        if letter in string.ascii_lowercase or letter in string.ascii_uppercase: 
            encryptedText += coder[letter]  
        else:
            encryptedText += letter                      
    return encryptedText