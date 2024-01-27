def single_letter_count(word, letter):
    
    count = 0
    for char in word:
        if char.lower() == letter.lower():
            count += 1
    print(count)
    
    
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

single_letter_count('Hello World', 'h')
single_letter_count('Hello World', 'z')
single_letter_count("Hello World", 'l')