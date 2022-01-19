def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAIEOU"
    out = ""
    reverse_string = s[::-1]
    reverse_vowels_in_string = []
    vowels_used = 0

    for char in reverse_string:
        if vowels.count(char) == 1:
            reverse_vowels_in_string.append(char)

    for char in s:
        if vowels.count(char) == 1:
            out = out + reverse_vowels_in_string[vowels_used]
            vowels_used = vowels_used + 1
        else:
            out = out + char

    return out

