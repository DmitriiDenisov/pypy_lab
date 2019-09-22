import numpy
import sklearn
import sys
from tqdm import tqdm
from time import time

print(sys.executable)

start = time()
l = [x ** 2 for x in tqdm(range(1, 10 ** 9))]
print(time() - start)
