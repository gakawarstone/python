 def search4vowels(phrase: str) -> set:
    """Return vowels pinned in aforementioned phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return array of letters from 'letters',
    pinned in aforementioned phrase."""
    return set(letters).intersection(set(phrase))
