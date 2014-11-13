from math import log, log1p, exp

__author__ = 'Deepak Borania'


def pv_factor(irate, period=1):
    return (1 + irate) ** (-period)


def convert_effective_rate(irate, src_prd_length, target_prd_length):
    return ((1 + irate) ** (float(target_prd_length) / src_prd_length)) - 1


def irate_nominal_to_effective(ip, p):
    return ((1 + (float(ip) / p)) ** p) - 1


def irate_effective_to_nominal(i, p):
    return p * (((1 + i) ** (1.0 / p)) - 1)


def drate_nominal_to_effective(dp, p):
    return 1 - ((1 - (float(dp) / p)) ** p)


def drate_effective_to_nominal(d, p):
    return p * (1 - ((1 - d) ** (1.0 / p)))


def irate_to_force(i):
    return log1p(i)


def irate_to_v(i):
    return pv_factor(i)


def irate_to_discrate(i):
    return i * pv_factor(i)


def force_to_irate(delta):
    return exp(delta) - 1


def force_to_v(delta):
    return exp(-delta)


def force_to_discrate(delta):
    return 1 - exp(-delta)


def v_to_force(v):
    return -log(v)


def v_to_irate(v):
    return (float(v) ** (-1)) - 1


def v_to_discount_rate(v):
    return 1 - v


def discount_rate_to_force(d):
    return -log(1 - d)


def discount_rate_to_irate(d):
    return ((1 - d) ** (-1)) - 1


def discount_rate_to_v(d):
    return 1 - d

