# Dokra
_Note_: We're currently still in Alpha phases, and invite you to contribute to Dokra!
###Take Type-Annotations To The Edge
A new syntax candy for you pythonista! 

Dokra allows using type hinting for middleware injection!
### How does it work?
Use type annotations to declare what functions will be executed __before__ the function on the parameters.
Use return type annotation to declare pipe-out function. 
```python
from Dokra import Dokra
d = Dokra()

def middleware(input_val):
    return input_val + 1

@Dokra
def my_func(value: d[middleware]) -> d[print]:
    return value + 1
```
### Installation
This requires Python3.6+


Install using pip:
```
pip install dokra
```
### Does this override type hinting?
No! We're utilizing slicing syntax to keep type hinting possible:
```python
@Dokra
def my_func(value: d[middleware: int]):
    return value + 1
```
### When is this useful?
This is just a syntax shortcut and may not always fit.
 Here's some of our suggestions:
* Similar type conversion (e.g - numpy array)
```python
@Dokra
def my_func(value: d[np.array]):
    ...
```
* Data validation
```python
@Dokra
def add_value(key: d[check_key], value: d[check_value]):
```
* Function chaining
```python
@Dokra
def my_func() -> d[logger]:
    return 'this line will be passed to logger function'
```