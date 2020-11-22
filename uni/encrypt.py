def encrypt(_str, n=5):
    _str = list(_str)
    _len = len(_str)
    k = (_len // n) + 1
    for i in range(k):
        _str.insert(i * (n + 1), '\t')
    _str = ''.join(_str)
    _str = _str.split('\t')
    _str = _str[1:]
    str_out = ''
    for i in _str:
        i = v_replace(i)
        str_out += i
    return str_out


def v_replace(_str, n=5):
    if len(_str) < n:
        return _str
    __str = list(_str)
    ___str = list(__str)
    __str[0] = ___str[2]
    __str[1] = ___str[3]
    __str[2] = ___str[1]
    __str[3] = ___str[4]
    __str[4] = ___str[0]
    __str = ''.join(__str)
    _str = __str
    return(_str)


print(encrypt(input()))
