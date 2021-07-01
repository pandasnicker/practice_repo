# read the tweets and filter them out based on keywords

import pandas as pd

data = pd.read_clipboard()
print(data.loc[1][0])