def list_check(lst):
    for item in lst:
        if not isinstance(item,list):
            return print(False)
    return print(True)


"""Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
list_check([[1], [2, 3]])
list_check([[1], "nope"])