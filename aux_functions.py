# aux functions 

import pandas as pd
import numpy as np


def create_frequency_table(df_control, df_test,name):
    
    # control
    frequency_table_control = df_control[name].value_counts()
   
    proportion_table_control = df_control[name].value_counts(normalize=True)
    
    # test
    frequency_table_test = df_test[name].value_counts()
   
    proportion_table_test = df_test[name].value_counts(normalize=True)
    
    return frequency_table_control, proportion_table_control, frequency_table_test, proportion_table_test