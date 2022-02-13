import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from PythonTsa.LjungBoxtest import plot_LB_pvalue
daxlogret = pd.read_csv('DAXlogret.csv', header = 0)
daxlogret.index = pd.DatetimeIndex(daxlogret.Date)
logret = daxlogret.Logret
logret.plot(title = 'Log returns of Germany DAX daily index')
plt.savefig('pyTSA_MarkovReturnsDAX_fig8-11.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
mod = sm.tsa.MarkovAutoregression(logret, k_regimes = 2, order = 1, switching_variance = True)
modfit = mod.fit()
print(modfit.summary())
modresid = modfit.resid
acf_pacf_fig(modresid, both = False, lag = 25)
plt.savefig('pyTSA_MarkovReturnsDAX_fig8-12.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
plot_LB_pvalue(modresid, noestimatedcoef = 0, nolags = 25)
plt.savefig('pyTSA_MarkovReturnsDAX_fig8-13.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 