import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from statsmodels.tsa.stattools import kpss
x = pd.read_csv('gdpquarterlychina1992.1-2017.4.csv', header = 0)
dates = pd.date_range(start = '1992', periods = len(x), freq = 'Q')
x.index = dates; x = pd.Series(x['GDP'])
dx = x.diff(4) # seasonal differencing
dx = dx.dropna()
dx.plot(marker = 'o', ms = 3) # ms means marker size
plt.savefig('pyTSA_GDPChinaDediff_fig3-4.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
d1dx = dx.diff(1)
d1dx = d1dx.dropna()
d1dx.plot(marker = 'o', ms = 3); 
plt.savefig('pyTSA_GDPChinaDediff_fig3-5.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
acf_pacf_fig(d1dx, both = False, lag = 44)
plt.savefig('pyTSA_GDPChinaDediff_fig3-6.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
kpss(d1dx, regression = 'c')
#InterpolationWarning: p-value is greater than the indicated p-value
#(0.20253789040706957, 0.1, 12, 
#{'10%': 0.347, '5%': 0.463, '2.5%': 0.574, '1%': 0.739})