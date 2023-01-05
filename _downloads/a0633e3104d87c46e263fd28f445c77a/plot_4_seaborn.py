# -*- coding: utf-8 -*-
r"""
Seaborn example
===============

This example demonstrates a Seaborn plot. Figures produced Matplotlib **and**
by any package that is based on Matplotlib (e.g., Seaborn), will be
captured by default. See :ref:`image_scrapers` for details.
"""
# Author: Michael Waskom & Lucy Liu
# License: BSD 3 clause

# %%
import sys
print([each for each in sys.modules if 'seaborn' in each])


# %%
import matplotlib
try:
    matplotlib.cm.get_cmap('rocket')
    print('rocket already registered')
except Exception:
    print('rocket does not exist')


# %%
import seaborn as sns
