import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from statsmodels.tsa.stattools import kpss
tem = pd.read_csv('Southtemperature.txt', header = None, sep = '\s+')
#read_table is deprecated, use read_csv instead.
temts = pd.concat([tem.loc[0], tem.loc[1]], ignore_index = 'true')
for i in range(2, 158):
    temts = pd.concat([temts, tem.loc[i]], ignore_index = 'true')
type(temts)
dates = pd.date_range('1850', periods = len(temts), freq = 'M')
temts.index = dates
temts.plot();
plt.savefig('pyTSA_TemperatureSH_fig3-1.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
dt = temts.diff(1) # the first differencing
dt = dt.dropna()
dt.plot() 
plt.savefig('pyTSA_TemperatureSH_fig3-2.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
acf_pacf_fig(dt, both = False, lag = 48)
plt.savefig('pyTSA_TemperatureSH_fig3-3.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
kpss(dt, regression = 'c')
