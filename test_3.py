import numpy
import sklearn
import sys
from tqdm import tqdm
from time import time
from math import sin

print(sys.executable)

start = time()
l = [sin(x) for x in tqdm(range(1, 10 ** 8))]
print(time() - start)
