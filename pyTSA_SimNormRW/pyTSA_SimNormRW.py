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
plt.savefig('pyTSA_SimNormRW_Fig1-13.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()