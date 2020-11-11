def solution1(big_array):
    count = 1
    while big_array:
        count *= len(set(big_array.pop()))
    return count

import numpy as np
def solution2(big_array):
    return np.prod(list(map(len,map(set,big_array))))

from functools import reduce
def solution3(big_array):
    return reduce(lambda x, y: x * y, list(map(lambda x: len(set(x)),big_array)))