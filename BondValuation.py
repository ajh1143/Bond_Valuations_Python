#----------------------------------
#Language: Python
#Function: bond_price(par_val, coup_rate, ttm, yld)
#Inputs: par_val for par value, coup_rate for coupon rate, ttm for time to maturity, and yld for yield
#Outputs: Dataframe,  Bond Price
#----------------------------------

import pandas as pd
import numpy as np
from pprint import pprint

def bond_price(par_val, coup_rate, ttm, yld):

#Create empty Dictionary to pass into Pandas DataFrame
    data = {'Cash_Flow': [],
                 'Time': [],
            'PV_Factor': [],
                   'PV': []
           }
    #Create DataFrame
    df = pd.DataFrame(data, columns=['Cash_Flow', 'Time', 'PV_Factor', 'PV'])
    #Generate Cash_Flow content
    cash_flow = np.array(np.repeat(int(par_val*coup_rate), ttm-1))
    #Push Cash_Flow records into DataFrame
    df.Cash_Flow = np.append(cash_flow, int(par_val*(1+coup_rate)))
    #Create Time record representing years, add to DataFrame
    df.Time = df.index+1
    #Create PV Factor, add to DataFrame
    df.PV_Factor = np.array(1/(1+yld)**df['Time'])
    #Create PV record and add to DataFrame
    df.PV = np.array(df.Cash_Flow * df.PV_Factor)
    #Set index to Time(Years)
    df.set_index('Time', inplace=True)
    #Return DataFrame and sum of PV column
    return df, sum(df.PV)

# Example set with par value = $100, coupon rate = %5, time to maturity = 5 years, and yield = %6
dataset, bondval = bond_price(100, 0.05, 5, 0.06)
pprint(dataset)
print("Total Bond Price: $" + str(bondval))
