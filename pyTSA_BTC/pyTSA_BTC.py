import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
bitcoin = pd.read_excel('BitcoinPrice17-6-23-18-6-22.xlsx', header = 0)
dat = pd.date_range('2017 06 23', periods = len(bitcoin),freq = 'D')
bitcoin.index = dat
price = bitcoin['ClosingP']
price.plot(); plt.title('Bitcoin Price 2017.6.23 2018.6.22')
plt.ylabel('Price in USD'); 
plt.savefig('pyTSA_BTC_Fig1-1.png', dpi = 1200, 
            bbox_inches ='tight', transparent = True); plt.show()
acf_pacf_fig(price, lag = 25)
plt.savefig('pyTSA_BTC_Fig1-14.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
logp = np.log(price)
logp.plot(); plt.title('Logarithm of the Bitcoin Price')
plt.ylabel('log(rice)')
plt.savefig('pyTSA_BTC_Fig1-15.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
acf_pacf_fig(logp, lag = 25)
plt.savefig('pyTSA_BTC_Fig1-16.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
dlogp = logp.diff(1)
dlogp = dlogp.dropna() #delete "NaN"
dlogp.plot()
plt.title('Difference of Logarithm of the Bitcoin Price')
plt.savefig('pyTSA_BTC_Fig1-17.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
acf_pacf_fig(dlogp, lag = 25); plt.savefig('pyTSA_BTC_Fig1-3.png', dpi = 1200, 
                      bbox_inches ='tight', transparent = True)
plt.savefig('pyTSA_BTC_Fig1-18.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()