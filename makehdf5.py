import pandas as pd
import h5py

#read a csv file into a pandas dataframe
df = pd.read_csv('data.csv')

#store the data from the dataframe into an HDF5 file
with pd.HDFStore('data.h5', mode='a') as store:
    store.append('data', df, format='table', data_columns=True)
    