def last_element(list):
    if len(list) <= 0:
        print("True")
    else:
        print(list.pop())
    
    
    
"""Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
"""
last_element([1,2,3])
last_element([])