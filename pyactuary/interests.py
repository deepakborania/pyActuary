from math import exp
from rateconverters import *
from scipy.integrate import quad
import numbers


def simple_interest_fi(present_val, irate, period):
    """
    Simple Interest on an amount with given interest rate in a given period
    :param present_val: Present Value
    :param irate: Interest Rate
    :param period: Time period
    :return:
    """
    return present_val * irate * period


def simple_interest_fv(p, irate, period):
    return p + simple_interest_fi(p, irate, period)


def compound_interest_fi(a, irate, period):
    return compound_interest_fv(a, irate, period) - a


def compound_interest_fv(a, irate, period):
    return a * (irate + 1) ** period


def pv(fv, irate, period):
    return fv * pv_factor(irate, period)


def pv_simple(future_val, discount_rate, period):
    return future_val * (1 - period * discount_rate)


def __arguments_check(force_function_list, period_list):
    if (not isinstance(force_function_list, list)) or (
            not all(hasattr(fn, '__call__') for fn in force_function_list)) or len(force_function_list) == 0:
        raise Exception('A list of functions expected')
    if (not isinstance(period_list, list)) or (
            not all(isinstance(period, numbers.Real) for period in period_list)) or len(period_list) == 0:
        raise Exception('A list of numbers expected')
    if not (len(period_list) == len(force_function_list) + 1):
        if len(force_function_list) == len(period_list) and period_list[0] != 0:
            period_list.insert(0, 0)
        else:
            raise Exception('Illegal period list')


def accumulation_factor_from_force_fn(force_function_list, period_list):
    __arguments_check(force_function_list, period_list)
    net_factor = 1
    for idx, force_function in enumerate(force_function_list):
        net_factor *= exp(quad(force_function, period_list[idx], period_list[idx + 1])[0])
    return net_factor


def pv_factor_from_force_fn(force_function_list, period_list):
    __arguments_check(force_function_list, period_list)
    net_factor = 1
    for idx, force_function in enumerate(force_function_list):
        net_factor *= exp(-quad(force_function, period_list[idx], period_list[idx + 1])[0])
    return net_factor

