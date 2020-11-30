import math

(x, y) = (int(input()) for i in range(2))
#
if x ** 2 + y ** 2 > 4 and x < 2:
    pass
#
if y < math.sin(x) and y < 0.5:
    pass
#
if (y > x and y ** 2 + x ** 2 < 1) or (y ** 2 + x ** 2 < 1 and y < x and x > 0):
    pass
#
if y < x ** 2 and y > 0:
    if x > 0:
        if y < 2 - x:
            pass
    else:
        if y > 2 - x:
            pass
#
if x > 0 and y < 1:
    if y > x - 1 or x ** 2 + y ** 2 < 1:
        pass
#
if x > 2 - x and y > 0:
    if x > 0:
        if y > x ** 2 and y < 4 - x ** 2:
            pass
    if x < 0:
        if x < x ** 2:
            pass
if x < 2 - x:
    if x > 0:
        if y < x ** 2:
            pass
    if x < 0:
        if y > x ** 2 and y < 4 - x ** 2:
            pass
#
if x ** 2 + y ** 2 < 1:
    if y > x and y > -x:
        pass
    if y < 0 and y > x and y > -x:
        pass
if x ** 2 + y ** 2 > 1:
    if y < 0 and y < x and y < - x:
        pass
