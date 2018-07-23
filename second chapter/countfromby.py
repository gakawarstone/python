class CountFromBy:

    def __init__(self, v: int, i: int) -> None:
        self.val = v
        self.incr = i

    def __repr__(self):
        return str(self.val)

    def increase(self) -> None:
        self.val += self.incr
