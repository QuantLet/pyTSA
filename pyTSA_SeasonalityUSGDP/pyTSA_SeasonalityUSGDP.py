import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.tools import diff
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from statsmodels.tsa.stattools import kpss
usgdp = pd.read_csv('usGDPnotAdjust.csv', header = 0)
timeindex = pd.date_range('1947-01', periods = len(usgdp), freq = 'QS')
usgdp.index = timeindex
usgdp = usgdp['NA000334Q']
lusgdp = np.log(usgdp)
lusgdp = lusgdp.rename('lusGDP')
lusgdp.plot()
plt.savefig('pyTSA_SeasonalityUSGDP_fig9-14.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
xdec = seasonal_decompose(lusgdp,  model = 'multi')
xdec.plot()
plt.savefig('pyTSA_SeasonalityUSGDP_fig9-15.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
myresid = xdec.resid.dropna()
myresid.plot()
plt.savefig('pyTSA_SeasonalityUSGDP_fig9-16.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
acf_pacf_fig(myresid,  both = True,  lag = 32)
plt.savefig('pyTSA_SeasonalityUSGDP_fig9-17.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
dmyresid = diff(myresid,  k_diff = 0,  k_seasonal_diff = 1, 
seasonal_periods = 4)
dmyresid.plot()
plt.savefig('pyTSA_SeasonalityUSGDP_fig9-18.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
acf_pacf_fig(dmyresid,  both = False,  lag = 32)
plt.savefig('pyTSA_SeasonalityUSGDP_fig9-19.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
kpss(dmyresid,  regression = 'c',  nlags = 'auto')
