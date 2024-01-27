def reverse_string(phrase):
    lists = list(phrase)
    lists.reverse()
    str = ""
    for li in lists:
        str += li
    
    print(str)
    
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
reverse_string('awesome')
reverse_string('sauce')