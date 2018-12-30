def hey(phrase):
    """Tests if the phrase (input) if it is in caps and ends with a question
    mark. Based on test results it will return a string.
    
    Input: can be anything, though will probably be a string
    
    Output: a string
    """    
    
    #Test 1: check if the phrase is in uppercase,while ignoring whitespace
    phrase = phrase.strip()
    uppercase = phrase.isupper()
    
    #Test 2: check if phrase ends with question mark
    question_mark = phrase.endswith("?")
    
    # Return reply based on results of Test 1 and Test 2
    if question_mark and not uppercase:
        return "Sure."
    elif uppercase and not question_mark:
        return "Whoa, chill out!"
    elif uppercase and question_mark:
        return "Calm down, I know what I'm doing!"
    elif phrase.isspace() or not phrase:
        return "Fine. Be that way!"
    else:
        return "Whatever."
    
