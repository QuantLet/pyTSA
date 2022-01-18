import pandas as pd
import numpy as np
bitcoin = pd.read_excel('BitcoinPrice 17 6 23 18 6 22.xlsx', header = 0)
dat = pd.date_range('2017 06 23', periods = len(bitcoin),freq = 'D')
bitcoin.index = dat
price = bitcoin['ClosingP']
import matplotlib.pyplot as plt
price.plot(); plt.title('Bitcoin Price 2017.6.23 2018.6.22')
plt.ylabel('Price in USD'); plt.show()
from PythonTsa.plot_acf_pacf import acf_pacf_fig
acf_pacf_fig(price, lag = 25)
logp = np.log(price)
logp.plot(); plt.title('Logarithm of the Bitcoin Price')
plt.ylabel('log(rice)'); plt.show()
acf_pacf_fig(logp, lag = 25)
dlogp = logp.diff(1)
dlogp = dlogp.dropna() #delete "NaN"
dlogp.plot()
plt.title('Difference of Logarithm of the Bitcoin Price')
plt.show()
acf_pacf_fig(dlogp, lag = 25)