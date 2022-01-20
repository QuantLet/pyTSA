[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **pyTSA_SimNormRW** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet:    'pyTSA_SimNormRW'

Published in:        'Applied Time Series Analysis and Forecasting with Python'

Description:         'This Quantlet generates three simulated paths of a standard Gaussian random walk'

Keywords:            'simulation, random walk, Gaussian, normal'

Author:              Huang Changquan, Alla Petukhina




```

![Picture1](pyTSA_SimNormRW_Fig1-13.png)

### PYTHON Code
```python

import numpy as np
import pandas as pd
from numpy.random import normal
import matplotlib.pyplot as plt
np.random.seed(1357)
a = normal(size = 300); b = normal(size = 300); c = normal(size = 300)
x = np.cumsum(a); y = np.cumsum(b); z = np.cumsum(c)
xyz = pd.DataFrame({'x': x, 'y': y, 'z': z})
xyz.index = range(1,301)
xyz.plot(style = ['-', '--', ':'])
plt.show()
```

automatically created on 2022-01-20