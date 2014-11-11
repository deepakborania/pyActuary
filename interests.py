from math import log, log1p, exp


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


def pv(fv, iRate, period):
    return fv * pvFactor(iRate, period)


def pvSimple(futureVal, discountRate, period):
    return futureVal * (1 - period * discountRate)


def convertEffectiveRate(iRate, srcPrdLength, targetPrdLength):
    return ((1 + iRate) ** (float(targetPrdLength) / srcPrdLength)) - 1


def iRateNominalToEffective(ip, p):
    return ((1 + (float(ip) / p)) ** p) - 1


def irateEffectiveToNominal(i, p):
    return p * (((1 + i) ** (1.0 / p)) - 1)


def dRateNominalToEffective(dp, p):
    return 1 - ((1 - (float(dp) / p)) ** p)


def dRateEffectiveToNominal(d, p):
    return p * (1 - ((1 - d) ** (1.0 / p )))


def iRateToForce(i):
    return log1p(i)


def iRateToV(i):
    return pvFactor(i)


def iRateToDiscRate(i):
    return i * pvFactor(i)


def forceToiRate(delta):
    return exp(delta) - 1


def forceToV(delta):
    return exp(-delta)


def forceToDiscRate(delta):
    return 1 - exp(-delta)


def vToForce(v):
    return -log(v)


def vToiRate(v):
    return (float(v) ** (-1)) - 1


def vToDiscRate(v):
    return 1 - v


def discRateToForce(d):
    return -log(1 - d)


def discRateToV(d):
    return 1 - d