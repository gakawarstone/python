import turtle as t


def go_snowy(length):
    if length < 1:
        t.forward(length)
    else:
        go_snowy(length / 3)
        t.left(60)
        go_snowy(length / 3)
        t.right(120)
        go_snowy(length / 3)
        t.left(60)
        go_snowy(length / 3)


# t.back(400)
# t.left(90)
# t.forward(300)
# t.right(90)
while(1):
    go_snowy(300)
    t.right(120)
