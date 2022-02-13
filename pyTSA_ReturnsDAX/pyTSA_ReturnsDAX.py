import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PythonTsa.LjungBoxtest import plot_LB_pvalue
dax = pd.read_csv('DAX.csv', header = 0)
dax.rename(columns = {'Adj Close' : 'index'}, inplace = True)
dax['logreturns'] = np.log(dax['index']/dax['index'].shift(1))
dax  =  dax.dropna()
logret  =  dax['logreturns']
logret.index  =  dax['Date']
fig  =  plt.figure()
dax['index'].plot(ax =  fig.add_subplot(211))
plt.ylabel('Dax daily index')
plt.xticks([])
logret.plot(ax =  fig.add_subplot(212))
plt.ylabel('Daily log return')
plt.xticks(rotation = 15)
plt.savefig('pyTSA_ReturnsDAX_fig6-5.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
plot_LB_pvalue(logret, noestimatedcoef = 0, nolags = 48)
plt.savefig('pyTSA_ReturnsDAX_fig6-6.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None)