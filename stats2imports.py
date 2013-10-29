# Imports for Statistical Computing
# http://mindey.com/blog/how_to_set_up_ipython_notebook_for_statistics_on_linux

import numpy as np  # For low level data structures (matrix, array,..)
import pandas as pd  # For high level data structures (vector, data.frame,...)
from pandas import Series, DataFrame  # Cause vectors and data frames are used so often!
import scipy as sp  # For special functions, including statistical distributions.
import statsmodels.api as sm  # For Statistical Computing (OLS, regressions, etc,...)
import sympy as sy  # For symbolic operations (integrating, differentiating,...)
import matplotlib.pyplot as plt  # For Plotting.
import pandas.rpy.common as rpy  # For interaction with R!
%load_ext rmagic  # For interaction with R!
a, b, c, x, y, z, t = sy.symbols("a b c x y z t")  # To avoid having to define symbols for symbolic ops.
k, m, n = sy.symbols("k m n", integer=True)  # Convenient when you want to integrate quicker.
f, g, h = sy.symbols("f g h", cls=sy.Function)  # And define functions quicker.
pd.set_option("notebook_repr_html", False)  # Often you don't want to see HTML tables, just text.
pd.set_option("max_rows",5000)  # Want to see more printed out in a DataFrame.
pd.set_option("max_columns",50)  # Want to see more columns in a DataFrame.
pd.set_option("display.max_columns", 50) # -- // --
pd.set_option("display.height", 10000) # -- // --
pd.set_option("display.width", 10000) # -- // --

#Want to have a quick function to send variables to R (thanks to Wes McKinney)
def to_r(df, name):
    from rpy2.robjects import r, globalenv
    r_df = rpy.convert_to_r_dataframe(df)
    globalenv[name] = r_df
