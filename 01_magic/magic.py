# draw a title and some text to the app

'''
# This is the document title

This is some _markdown_

'''

import streamlit as st

import pandas as pd

df: pd.DataFrame = pd.DataFrame({ "col1": [1, 2 , 3], 'col2': list("abc") })

df   # 👈 draw the dataframe

x: int = 100

"x", x    # 👈 draw the string 'x' and then the value of x


# Short Break


# Also works with most supported chart type

import matplotlib.pyplot as plt

import numpy as np

arr = np.random.normal(1, 1, size=100)

fig, ax = plt.subplots()

ax.hist(arr, bins=30)

fig    # 👈 draw a matplotlib chart

'# Pakistan Zindabad!'

# Hello World

'''
# This is a document title

this is some _markdown_
'''
