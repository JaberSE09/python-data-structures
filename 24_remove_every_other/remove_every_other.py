def remove_every_other(lst):
    return print([val for i, val in enumerate(lst) if i %2 ==0])
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

lst = [1, 2, 3, 4, 5]
remove_every_other(lst)