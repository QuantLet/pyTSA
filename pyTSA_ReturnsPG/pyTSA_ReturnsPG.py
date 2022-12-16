import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from statsmodels.tsa.stattools import acf
x = pd.read_table('monthly returns of Procter n Gamble stock n 3 market indexes 1961 to 2016.csv', 
                  sep = ',', header = 0)
timeindex = pd.date_range('1961', periods = len(x), freq = 'M')
x.index = timeindex
yts = x['RET']
yts.plot(); 
plt.savefig('pyTSA_ReturnsPG_fig2-8.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
yts.describe()
pd.Series.idxmax(yts) # get the position of the maximum
#Timestamp('1998-10-31 00:00:00', freq = 'M')
pd.Series.idxmin(yts) # get the position of the minimum
#Timestamp('2000-03-31 00:00:00', freq = 'M')
acf_pacf_fig(yts, both = True, lag = 17)
plt.savefig('pyTSA_ReturnsPG_fig2-9.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
r,q,p = acf(yts,qstat = True)
p