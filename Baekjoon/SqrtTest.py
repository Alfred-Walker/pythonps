import timeit

my_setup = "import math"
print("744 ** 0.5: {0}".format(min(timeit.Timer('744 ** 0.5', setup=my_setup).repeat(7, 1000))))
print("math.sqrt(744): {0}".format(min(timeit.Timer('math.sqrt(744)', setup=my_setup).repeat(7, 1000))))

