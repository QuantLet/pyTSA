[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **pyTSA_GaussWN** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet:    'pyTSA_GaussWN'

Published in:        'Applied Time Series Analysis and Forecasting with Python'

Description:         'This Quantlet generates Gaussian white noise'

Keywords:            'simulation, white noise, Gaussian, normal'

Author:              Huang Changquan, Alla Petukhina




```

![Picture1](pyTSA_GaussWN_fig1-10.png)

![Picture2](pyTSA_GaussWN_fig1-9.png)

### PYTHON Code
```python

from numpy import random
import pandas as pd
random.seed(135) # for repeat
x=random.normal(loc=0, scale=1, size=1000)
xts=pd.Series(x)
import matplotlib.pyplot as plt
xts.plot(); plt.xlabel('Time')
plt.ylabel('Simulated white noise'); plt.show()
from PythonTsa.plot_acf_pacf import acf_pacf_fig
acf_pacf_fig(xts, both=False, lag=30)
```

automatically created on 2022-01-20