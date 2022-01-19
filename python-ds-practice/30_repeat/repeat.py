def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    if isinstance(num, int) == False or num < 0 :
        return None
    repeated_phrase = ""
    for i in range(0, num):
        repeated_phrase = repeated_phrase + phrase

    return repeated_phrase

