import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import month_plot
from statsmodels.tsa.seasonal import seasonal_decompose
from PythonTsa.plot_acf_pacf import acf_pacf_fig
aul = pd.read_excel('AustraliaEmployedTotalPersons.xlsx', header = 0)
timeindex = pd.date_range('1978-02',periods = len(aul),freq = 'M')
aul.index = timeindex
aults = aul['EmployedP']
aults.plot(); 
plt.savefig('pyTSA_AustralianLabour_fig2-13.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True);
plt.show()
# Graph time series plot from 2013.1 to 2017.1
aults['2013-01':'2017-01'].plot(); 
plt.savefig('pyTSA_AustralianLabour_fig2-14.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True); plt.show()
month_plot(aults);
plt.savefig('pyTSA_AustralianLabour_fig2-15.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True); plt.show() #Plot seasonal plots
aultsdeca = seasonal_decompose(aults, model = 'additive')
aultsdeca.plot(); 
plt.savefig('pyTSA_AustralianLabour_fig2-16.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True); plt.show()
df = pd.DataFrame(data = { 'resid'  : aultsdeca.resid})
df = df.dropna()
acf_pacf_fig(df, both = False, lag = 48)
plt.savefig('pyTSA_AustralianLabour_fig2-17.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True);
ar = df
rolm = pd.Series.rolling(ar, window = 36, center = True).mean()
rolstd = pd.Series.rolling(ar, window = 36, center = True).std()
plt.plot(aultsdeca.resid, label = 'dec resid')
plt.plot(rolm, label = 'resid roll mean', linestyle = '--' )
plt.plot(rolstd, label = 'resid roll std', linestyle = ':')
plt.title('Add. decom. resid. of Australian employed persons')
plt.legend()
plt.savefig('pyTSA_AustralianLabour_fig2-18.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True); plt.show()