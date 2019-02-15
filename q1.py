'''
implement a function/method that is given two strings and returns whether one can be obtained by the other after removing exactly one character. Specifically, given two strings x and y, return true if and only if (1) x can be obtained by removing one character from y and/or (2) if y can be obtained by removing one character from x. Assume that both strings only contain English alphabets and that neither is an empty string. Note that x and y can be quite long (each containing millions of characters).
'''

# Python:
def equalsWhenOneCharRemoved(x, y):
    '''
    >>> equalsWhenOneCharRemoved("x", "y")
    False
    >>> equalsWhenOneCharRemoved("x", "XX")
    False
    >>> equalsWhenOneCharRemoved("yy", "yx")
    False
    >>> equalsWhenOneCharRemoved("abcd", "abxcd")
    True
    >>> equalsWhenOneCharRemoved("xyz", "xz")
    True
    '''
    lx, ly = len(x), len(y)
    # for early termination
    if abs(lx-ly) != 1:
        return False

    i = j = 0
    removed = False
    # scan
    while i < lx and j < ly:
        if x[i] != y[j]:
            # removed previously? then donen with the iteration
            if removed:
                return False
            if lx > ly:
                i += 1
            else:
                j += 1
            removed = True
        else:
            i += 1
            j += 1
    return True
