import numpy as np
from time import perf_counter

list1 = [np.random.rand() for _ in range(1000000)]
list2 = [np.random.rand() for _ in range(1000000)]

start_lists = perf_counter()
result_list = [a * b for a, b in zip(list1, list2)]
end_lists = perf_counter()
time_lists = end_lists - start_lists

array1 = np.random.rand(1000000)
array2 = np.random.rand(1000000)

start_arrays = perf_counter()
result_array = np.multiply(array1, array2)
end_arrays = perf_counter()
time_arrays = end_arrays - start_arrays

print("Время выполнения для стандартных списков:", time_lists, "секунд")
print("Время выполнения для массивов NumPy:" ,time_arrays, "секунд")
