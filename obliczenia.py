import numpy as np

oned_array = ([1, 2, 3, 4, 5])

secd_array = (
    [1, 'a'],
    [2, 'b'],
    [3, 'c'],
    [4, 'd']
)

my_array = np.array([1, 2, 3, 4, 5])
print(type(my_array))
print(my_array.shape)
print(my_array.size)
print(len(my_array))
print(my_array.dtype)
print(my_array.astype(float))
print(my_array[0])
print(my_array.sum())
print(my_array.min())
print(my_array.max())
print(my_array.mean())

input_stock_price_array = np.genfromtxt('pliki/AAPL_stock_price_example.csv', delimiter=',', skip_header=1,
                                        usecols=(1,))
print(input_stock_price_array.size)
# print(input_stock_price_array)
sorted_input_stock_price = np.sort(input_stock_price_array)[::-1]
print(sorted_input_stock_price[:5])
print(sorted_input_stock_price.shape)

a = np.array([1, 2, 3, -4, 5, 6])
c = a * 10
print(c)

d = np.arange(1, 27, step=3) - 7 * 2
print(d)

zero = np.zeros((5, 4, 3), dtype='int')
print(zero)

b = a.reshape((2, 3))
print(b)

my_3d = np.arange(70)
my_3d.shape = (2, 7, 5)
my_3d2 = 5 * my_3d - 2
left = np.arange(6).reshape((2, 3))
right = np.arange(15).reshape((3, 5))
do = np.dot(left, right)
print(do)

my_ran_arr = np.random.random((7, 5))
print(my_ran_arr)

person_data = [('name', 'S6'), ('height', 'f8'), ('weight', 'f8'), ('age', 'i8')]
people = np.zeros((4,), dtype=person_data)
people[3] = ('Delta', 73, 205, 34)
print(people.dtype)
