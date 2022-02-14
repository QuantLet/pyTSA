import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.graphics.tsaplots import quarter_plot
sar1 = np.array([1, 0, 0, 0, -0.2])
sar2 = np.array([1, 0, 0, 0, -0.6])
sar3 = np.array([1, 0, 0, 0, -0.8])
sar4 = np.array([1, 0, 0, 0, -1.0])
np.random.seed(137)
x1 = arma_generate_sample(ar = sar1, ma = [1], nsample = 200)
x2 = arma_generate_sample(ar = sar2, ma = [1], nsample = 200)
x3 = arma_generate_sample(ar = sar3, ma = [1], nsample = 200)
x4 = arma_generate_sample(ar = sar4, ma = [1], nsample = 200)
x1 = pd.Series(x1); x2 = pd.Series(x2)
x3 = pd.Series(x3); x4 = pd.Series(x4)
fig = plt.figure()
x1.plot(marker = '.', ax = fig.add_subplot(221))
plt.title('$X_t = 0.2X_{t-4}+\epsilon_t$')
x2.plot(marker = '.', ax = fig.add_subplot(222))
plt.title('$X_t = 0.6X_{t-4}+\epsilon_t$')
x3.plot(marker = '.', ax = fig.add_subplot(223))
plt.title('$X_t = 0.8X_{t-4}+\epsilon_t$')
x4.plot(marker = '.', ax = fig.add_subplot(224))
plt.title('$X_t = 1.0X_{t-4}+\epsilon_t$')
plt.savefig('pyTSA_Seasonality_fig9-9.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
fig = plt.figure()
ax = fig.add_subplot(221)
acf_pacf_fig(x1, both = False, lag = 16)
plt.title('$X_t = 0.2X_{t-4}+\epsilon_t$')
ax = fig.add_subplot(222)
acf_pacf_fig(x2, both = False, lag = 16)
plt.title('$X_t = 0.6X_{t-4}+\epsilon_t$')
ax = fig.add_subplot(223)
acf_pacf_fig(x3, both = False, lag = 16)
plt.title('$X_t = 0.8X_{t-4}+\epsilon_t$')
ax = fig.add_subplot(224)
acf_pacf_fig(x4, both = False, lag = 16)
plt.title('$X_t = 1.0X_{t-4}+\epsilon_t$')
plt.savefig('pyTSA_Seasonality_fig9-10.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
speriod = pd.date_range('2001-01', periods = len(x1), freq = 'Q')
x1.index = speriod
x2.index = speriod
x3.index = speriod
x4.index = speriod
fig = plt.figure()
quarter_plot(x1, ax = fig.add_subplot(221))
plt.title('Seasonal plot for $X_t = 0.2X_{t-4}+\epsilon_t$')
quarter_plot(x2, ax = fig.add_subplot(222))
plt.title('Seasonal plot for $X_t = 0.6X_{t-4}+\epsilon_t$')
quarter_plot(x3, ax = fig.add_subplot(223))
plt.title('Seasonal plot for $X_t = 0.8X_{t-4}+\epsilon_t$')
quarter_plot(x4, ax = fig.add_subplot(224))
plt.title('Seasonal plot for $X_t = 1.0X_{t-4}+\epsilon_t$')
plt.savefig('pyTSA_Seasonality_fig9-11.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
y = pd.DataFrame(index = range(0, int(len(x1)/4)), 
columns = ['0', '1', '2', '3'])
for i in range(0, 4):
    for j in range(i, len(x1), 4):
        y.iat[int(j/4), i] = x1[j]
z = pd.concat([y['0'], y['1'], y['2'], y['3']], ignore_index = True)
fig = plt.figure()
ax = fig.add_subplot(211)
z.plot()
plt.title('The concatenate series of the seasonal subseries for $X_t = 0.2X_{t-4}+\epsilon_t$')
ax = fig.add_subplot(212)
acf_pacf_fig(z, both = False, lag = 16)
plt.savefig('pyTSA_Seasonality_fig9-12.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
srw = pd.DataFrame(index = range(0, int(len(x1)/4)), 
columns = ['0', '1', '2', '3'])
for i in range(0, 4):
    for j in range(i, len(x4), 4):
        srw.iat[int(j/4), i] = x4[j]
csrw = pd.concat([srw['0'], srw['1'], srw['2'], srw['3']], ignore_index = True)
fig = plt.figure()
ax = fig.add_subplot(211)
csrw.plot()
plt.title('The concatenate series of the seasonal subseries for $X_t = 1.0X_{t-4}+\epsilon_t$')
ax = fig.add_subplot(212)
acf_pacf_fig(csrw, both = False, lag = 16)
plt.savefig('pyTSA_Seasonality_fig9-13.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 