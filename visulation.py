import numpy as np
import pandas as pd
a = pd.Series([1, 3.14,5,np.nan,6 ])
print(a)

lastweekdata = pd.date_range('20200413', periods=7)
print(lastweekdata)
df = pd.DataFrame(np.random.randn(7,7), index=lastweekdata, columns=list('1234567'))
print(df)


