def simpleIntrFI(p, i, t):
    return p * i * t


def simpleIntrFV(p, i, t):
    return p + simpleIntrFI(p, i, t)


def cmpdIntrFI(a, i, n):
    return cmpdIntrFV(a, i, n) - a


def cmpdIntrFV(a, i, n):
    return a * (i + 1) ** n


def pvFactor(i, n=1):
    return (1 + i) ** (-n)


def pv(c, i, n):
    return c * pvFactor(i, n)


def pvSimple(c, d, n):
    return c * (1 - n * d)


print pvSimple(100000, 0.15, 8./12)
