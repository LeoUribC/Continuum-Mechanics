# file for testing purposes, can be deleted later

import pandas as pd
import numpy as np

colNumbers = 5

def generateRandomData(s):
    return np.random.uniform(size=s)

data = {
    'column 1':[1, 2, 3],
    'column 2':[4, 5, 6],
    'column 3':[7, 8, 9]
}

print(
    pd.DataFrame(data=data, index=range(3))
)