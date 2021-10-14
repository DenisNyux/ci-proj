from integrals import IntegralMethods

i = IntegralMethods()

assert type(i.parabola(-10, 10)) == float
assert type(i.trapeze(-10, 10)) == float
assert round(i.parabola(-10, 10), 5) == 3662.928
assert round(i.trapeze(-10, 10), 5) == 3900.002

