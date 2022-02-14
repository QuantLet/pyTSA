import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from PythonTsa.LjungBoxtest import plot_LB_pvalue
IBM = pd.read_csv('IBM.csv', header = 0)
IBM['Date'] = pd.to_datetime(IBM['Date'])
IBM.index = IBM['Date']
IBMclose = IBM.Close
LIBMclose = np.log(IBMclose)
LIBMclose.plot()
plt.xticks(rotation = 15)
plt.savefig('pyTSA_TrendIBM_fig9-5.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
dLIBMclose = LIBMclose.diff(1).dropna()
dLIBMclose.plot()
plt.savefig('pyTSA_TrendIBM_fig9-6.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
acf_pacf_fig(dLIBMclose, both = False, lag = 20)
plt.savefig('pyTSA_TrendIBM_fig9-7.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
plot_LB_pvalue(dLIBMclose, noestimatedcoef = 0, nolags = 30)
plt.savefig('pyTSA_TrendIBM_fig9-8.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
