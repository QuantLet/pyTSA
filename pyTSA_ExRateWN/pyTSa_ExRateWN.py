import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from statsmodels.stats.diagnostic import acorr_ljungbox
x = pd.read_table('ExchRate NZ per UK.txt', header=0)
dates = pd.date_range('1991', periods = len(x), freq = 'Q')
x.index = dates; xts = pd.Series(x['xrate'])
logxts = np.log(xts)
dlogxts = logxts.diff(1)
dlogxts = dlogxts.dropna() #delete "NaN"
dlogxts.plot(marker = 'o', markersize = 5)
plt.title('Difference of Logarithm of the ExchRate NZ per UK')
plt.savefig('pyTSA_ExRateWN_fig2-5.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True); plt.show()
acf_pacf_fig(dlogxts, both = False, lag = 17)
plt.savefig('pyTSA_ExRateWN_fig2-6.png', dpi = 1200, 
            bbox_inches ='tight', transparent = True);
r,q,p = acf(dlogxts,nlags = 35,qstat = True)
#r for ACF; q for Ljung-Box statistics; p for p-values
p
q1,p1 = acorr_ljungbox(dlogxts, lags = 35, boxpierce = False)
p1
ddlogxts = dlogxts.diff(1)
ddlogxts = ddlogxts.dropna()
acf_pacf_fig(ddlogxts, both = False, lag = 17)
plt.savefig('pyTSA_ExRateWN_fig2-7.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True); plt.show()
r2,q2,p2 = acf(ddlogxts,nlags = 35,qstat = True)
p2