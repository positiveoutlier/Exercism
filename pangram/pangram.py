def is_pangram(sentence):
    """
    This function checks if the input is a pangram. A pangram
    is a sentence that uses every letter of the alphabet at least once.
    
    Input: 
        sentence = a string that will not contain non-ASCII symbols
        
    Returns:
        True if the input is a pangram
        False if the input is not a pangram
    """
    
    sentence = [c.lower() for c in sentence if c.isalpha()]
    sentence = ''.join(sentence)
    
    tracker = []
    
    for c in sentence:
        if c not in tracker:
            tracker += c
    
    if len(tracker) == 26:
        return True
    else:
        return False
    
