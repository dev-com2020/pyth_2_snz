from ctypes import cdll, c_int

lib = cdll.LoadLibrary('/Users/tomaszkaniecki/PycharmProjects/pyth_2_snz/counter2.cpython-311-darwin.so')

lib.count_primes.argtypes = [c_int]
lib.count_primes.restypes = c_int

result = lib.count_primes(10000)
print(result)
