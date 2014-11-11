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
