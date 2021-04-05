import pandas as pd
import numpy as np
import math

df=pd.DataFrame({'Class': ['A1','A1','A1','A2','A3','A3'],
                 'Force': [50,150,100,120,140,160] },
                 columns=['Class', 'Force'])
print(df)
print('-'*30)

stats = df.groupby(['Class'])['Force'].agg(['mean', 'count', 'std'])
print(stats)
print('-'*30)

ci95_hi = []
ci95_lo = []

for i in stats.index:
    m, c, s = stats.loc[i]

    asdd = 1.95*s/math.sqrt(c)
    ci95_hi.append(m + 1.95*s/math.sqrt(c))
    ci95_lo.append(m - 1.95*s/math.sqrt(c))

stats['ci95_hi'] = ci95_hi
stats['ci95_lo'] = ci95_lo
print(stats)