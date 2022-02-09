[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **pyTSA_Chaos** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet:    'pyTSA_Chaos'

Published in:        'Applied Time Series Analysis and Forecasting with Python'

Description:         'This Quantlet produces Chaos like a White Noise and saves in csv file'

Keywords:            'time series, White noise, ACF, PACF, simulation'

Author:              Huang Changquan, Alla Petukhina




```

### PYTHON Code
```python

import pandas as pd
import numpy as np
x = pd.Series(dtype = float)
y = 0.3 # start value
for t in range(1, 501):
    y = 4.0 * y * (1 - y)
    x = x.append(pd.Series(y))
index = range(1, 501)
x.index = index
np.savetxt('Chaos.csv', np.column_stack((x.index, x)), delimiter=',')
```

automatically created on 2022-02-09