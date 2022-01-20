[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **pyTSA_ARMA** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet:    'pyTSA_ARMA'

Published in:        'Applied Time Series Analysis and Forecasting with Python'

Description:         'This Quantlet simulates and plots ARMA(2,2) - autoregressive moving average process time series, its ACF and PACF'

Keywords:            'time series,  stationarity, autocorrelation, PACF, ACF, simulation, stochastic process, ARMA, moving average, autoregression'

Author[New]:         Huang Changquan, Alla Petukhina




```

![Picture1](SimulatedARMA4SampleACF.png)

![Picture2](pyTSA_ARMA_fig3-19.png)

![Picture3](pyTSA_ARMA_fig3-20.png)

### PYTHON Code
```python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import arma_generate_sample
from PythonTsa.plot_acf_pacf import acf_pacf_fig
ar = np.array([1, -0.8, 0.6])
ma = np.array([1, 0.7, 0.4])
np.random.seed(123457)
x =  arma_generate_sample(ar = ar, ma = ma, nsample = 500)
x = pd.Series(x)
x.plot(); plt.savefig('TSP_ARMA_fig3-19.png'), plt.show()
acf_pacf_fig(x, both = True, lag=50)
```

automatically created on 2022-01-20