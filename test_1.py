import numpy
import sklearn
import sys
from tqdm import tqdm
from time import time
print(sys.executable)


def sum_up_to_n(n):
    a = 0
    for i in tqdm(range(n)):
        a += i
    return a

start = time()
sum_up_to_n(10 ** 9)
print(time() - start)
