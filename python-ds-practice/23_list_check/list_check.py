def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    all_items = True
    for element in lst:
        if isinstance(element, list) == False:
            all_items = False

    return all_items

