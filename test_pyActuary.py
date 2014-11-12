from pyactuary.interests import *

# Test Scripts
def integrand1(x):
    return 0.08


def integrand2(x):
    return 0.13 - 0.01 * x


print accumulation_factor_from_force_fn([integrand1, integrand2], [0, 5, 10]) * 1000

print pv_factor_from_force_fn([integrand1, integrand2], [0, 5, 10]) * 1964.03297597