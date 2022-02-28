[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **pyTSA_SARMA** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet:    'pyTSA_SARMA'

Published in:        'Applied Time Series Analysis and Forecasting with Python'

Description:         'This Quantlet simulates ARMA(2,2) - autoregressive moving average process and draws the true ACF and PACF'

Keywords:            'time series,  stationarity, autocorrelation, PACF, ACF, simulation, stochastic process, ARMA, moving average, autoregression'

Author[New]:         Huang Changquan, Alla Petukhina




```

![Picture1](pyTSA_SARMA_fig5-6.png)

![Picture2](pyTSA_SARMA_fig5-7.png)

![Picture3](pyTSA_SARMA_fig5-8.png)

### PYTHON Code
```python

import numpy as np
from PythonTsa.True_acf import Tacf_pacf_fig
import matplotlib.pyplot as plt
ar1 = np.array([1, 0, 0, 0, -0.36])
Tacf_pacf_fig(ar = ar1, ma = [1], both = True, lag = 20)
plt.savefig('pyTSA_SARMA_fig5-6.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None);
ma1 = np.array([1,0,0,0,0.46])
Tacf_pacf_fig(ar = [1], ma = ma1, both = True, lag = 20)
plt.savefig('pyTSA_SARMA_fig5-7.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None);
Tacf_pacf_fig(ar = ar1, ma = ma1, both = True, lag = 20)
plt.savefig('pyTSA_SARMA_fig5-8.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None);

```

automatically created on 2022-02-28