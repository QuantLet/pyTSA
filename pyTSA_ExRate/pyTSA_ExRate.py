import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from PythonTsa.plot_acf_pacf import acf_pacf_fig
x = pd.read_table('ExchRate NZ per UK.txt', header=0)
dates = pd.date_range('1991', periods = len(x), freq = 'Q')
x.index = dates; xts = pd.Series(x['xrate'])
xts.plot(); plt.xlabel('Years')
plt.ylabel('Exchange rate');
plt.savefig('pyTSA_ExRate_fig2-1.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True);
# The following is to plot ACF and PACF using statsmodels
fig = plt.figure()
plot_acf(xts, lags = 17, ax = fig.add_subplot(2, 1, 1))
plot_pacf(xts, lags = 17, ax = fig.add_subplot(2, 1, 2))
fig.tight_layout(pad = 1.5);
plt.savefig('pyTSA_ExRate_fig2-2.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True);
# The following is to plot ACF and PACF using PythonTsa
acf_pacf_fig(xts, both = True, lag = 17)
plt.savefig('pyTSA_ExRate_fig2-3.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True);