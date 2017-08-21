import pandas as pd
import numpy as np

def summary(df):
    "Pass a pandas DataFrame and get better information about missing values."
    summary = pd.DataFrame(columns=['entries', 'null_entries', 'unique_entries', 'data_type', 'memory_usage(kb)'])
    summary['memory_usage(kb)'] = [i/1000 for i in (list(df.memory_usage())[1:])]
    summary.index = list(df.columns)
    summary['entries'] = [df[i].notnull().sum() for i in df.columns]
    summary['null_entries'] = [df[i].isnull().sum() for i in df.columns]
    summary['unique_entries'] = [len(df[i].unique()) for i in df.columns]
    summary['data_type'] = [df[i].dtypes for i in df.columns]
    print " "
    print 'ROWS =', list(df.shape)[0], ' |  COLUMNS =', list(df.shape)[1]
    print summary
