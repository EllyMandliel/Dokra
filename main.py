from dokra import Dokra
import numpy as np

'''
d = Dokra()


def convert_to_numpy_array(in_iterator):
    return np.array(list(in_iterator))


def some_output_function(output):
    print(f'[20-10-2020 15:46] Info: Received {output}')


@Dokra
def final_func(my_array: d[convert_to_numpy_array: np.array]) -> d[some_output_function]:
    return my_array.sum()


# Assign all changes
final_func(range(50))
'''

from dokra import Dokra

d = Dokra()


def middleware(input_val):
    return input_val + 1


@Dokra
def my_func(value: d[middleware]) -> d[print]:
    return value + 1
