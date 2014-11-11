def simpleIntrFI(p, iRate, period):
    return p * iRate * period


def simpleIntrFV(p, iRate, period):
    return p + simpleIntrFI(p, iRate, period)


def cmpdIntrFI(a, iRate, period):
    return cmpdIntrFV(a, iRate, period) - a


def cmpdIntrFV(a, iRate, period):
    return a * (iRate + 1) ** period


def pvFactor(iRate, period=1):
    return (1 + iRate) ** (-period)


def pv(c, iRate, period):
    return c * pvFactor(iRate, period)


def pvSimple(c, d, period):
    return c * (1 - period * d)


def convertEffectiveRate(iRate, srcPrdLength, targetPrdLength):
    return ((1 + iRate) ** (float(targetPrdLength) / srcPrdLength)) - 1
