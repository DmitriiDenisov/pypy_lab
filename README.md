# pypy_lab

### What is pypy?
https://youtu.be/1n9KMqssn54


### Installation:
1. Download https://pypy.org/download.html
2. Unzip it
3. Run from bin/pypy3

### Perfomance:
Run test_1.py, test_2.py, test_3.py files with CPython and Pypy for comparison. Basically Pypy is ~2 times fater than CPython

### Useful commands:

Install pip:
```bin/pypy3 -m ensurepip```

Install packages:
```bin/pypy3 -m pip install pandas```
```bin/pypy3 -m pip install scikit-learn```

If error with sklearn try: 
```bin/pypy3 -m pip install --upgrade cython```


### List of supported packages for pypy:
http://packages.pypy.org/##numpy
