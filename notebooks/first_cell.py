%reload_ext autoreload
%autoreload 2

import os
import sys
sys.path.insert(0, '../')
from config import RAW_PATH, TREAT_PATH, OUTPUT_PATH

import os
from copy import deepcopy
import numpy as np
import pandas as pd
pd.options.display.max_columns = 999
import pandas_profiling

import warnings
warnings.filterwarnings('ignore')

# Plotting
import matplotlib.pyplot as plt

import plotly
import plotly.graph_objs as go
import cufflinks as cf
plotly.offline.init_notebook_mode(connected=True)

cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)