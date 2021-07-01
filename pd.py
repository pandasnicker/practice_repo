import pandas as pd
import numpy as np

df = pd.read_sas(r'C:\Users\mgula\Downloads\airline.sas7bdat')

print(df.head(2))
print("Total number of records: ", len(df)-1)