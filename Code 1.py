import datetime
import math

import numpy as np
import pandas as pd
import tensorflow as tf

print('Hello World')

def calculate(x):
    result = 2 * x
    return result

calculate(3)
calculate(4)

def calculate_circle(x):
    result = math.pi * (x**2)
    return result

def calculate_triangle(b,h):
    result = 1/2 * b * h
    return result

def calculate_rectangle(l,b):
    result = l * b
    return result
    