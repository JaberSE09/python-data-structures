def multiple_letter_count(phrase):
    letter_counts = {}
    for letter in phrase:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1  
    print(letter_counts)


    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
multiple_letter_count('yay')
multiple_letter_count('Yay')
    