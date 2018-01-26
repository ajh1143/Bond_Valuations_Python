#----------------------------------
#Language: Python
#Function: bond_price(p,r,ttm,y)
#Inputs: p for par value, r for coupon rate, ttm for time to maturity, and y for yield
#Outputs: Dataframe,  Bond Price
#----------------------------------

import pandas as pd
import numpy as np
from pprint import pprint

def bond_price(par_val, coup_rate, ttm, yld):

    data = {'Cash_Flow': [],
                 'Time': [],
            'PV_Factor': [],
                   'PV': []
           }
    df = pd.DataFrame(data, columns=['Cash_Flow', 'Time', 'PV_Factor', 'PV'])
    cash_flow = np.array(np.repeat(int(par_val*coup_rate), ttm-1))
    df.Cash_Flow = np.append(cash_flow, int(par_val*(1+coup_rate)))
    df.Time = df.index+1
    df.PV_Factor = np.array(1/(1+yld)**df['Time'])
    df.PV = np.array(df.Cash_Flow * df.PV_Factor)
    df.set_index('Time', inplace=True)
    return df, sum(df.PV)

# Example set 
dataset, bondval = bond_price(100, 0.05, 5, 0.06)
pprint(dataset)
print("Total Bond Price: $" + str(bondval))