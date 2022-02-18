import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint, adfuller
from statsmodels.tsa.vector_ar.vecm import VECM,  select_coint_rank, select_order#coint_johansen,
from PythonTsa.plot_multi_ACF import multi_ACFfig
from PythonTsa.plot_multi_Q_pvalue import MultiQpvalue_plot
bwoil = pd.read_csv('WTI-Brent.csv')
dates = pd.date_range('1987-05', periods = len(bwoil), freq = 'M')
bwoil.index = dates
bwoil.plot(style = ['-', ':'])
plt.savefig('pyTSA_CointegrationOil_fig9-30.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
logbw = np.log(bwoil)
logbw.columns = ['LBrent', 'LWTI']
logbw.plot(style = ['-', ':'])
plt.savefig('pyTSA_CointegrationOil_fig9-31.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
multi_ACFfig(logbw, nlags = 18)
plt.savefig('pyTSA_CointegrationOil_fig9-32.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
adfuller(logbw.LWTI, regression = 'c')
adfuller(logbw.LBrent, regression = 'c')
dlogbw = logbw.diff(1).dropna()
dlogbw.columns = ['DLBrent', 'DLWTI']
dlogbw.plot(style = ['-', ':'])
plt.savefig('pyTSA_CointegrationOil_fig9-33.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
multi_ACFfig(dlogbw, nlags = 18)
plt.savefig('pyTSA_CointegrationOil_fig9-34.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
coint(logbw.LWTI, logbw.LBrent, trend = 'c')
selord = select_order(data = logbw, maxlags = 10, deterministic = 'co')
selord.selected_orders
scr = select_coint_rank(logbw, det_order = 0, k_ar_diff = 2)
print(scr.summary())
scr.rank
vecmod = VECM(endog = logbw, k_ar_diff = 2, coint_rank = 1, deterministic = 'co')
vecmfit = vecmod.fit()
print(vecmfit.summary())
vecmresid = vecmfit.resid
multi_ACFfig(vecmresid, nlags = 18)
plt.savefig('pyTSA_CointegrationOil_fig9-35.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
q, p = MultiQpvalue_plot(vecmresid, p = 3, q = 0, noestimatedcoef = 10, nolags = 24)
plt.savefig('pyTSA_CointegrationOil_fig9-36.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()