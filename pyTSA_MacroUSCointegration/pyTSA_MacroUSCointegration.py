import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.tsa.stattools import coint, adfuller, kpss
#import statsmodels.api as sm
usm = pd.read_table('USmacronInRate.txt', sep = '\s+', header = 0)
usm = usm[['rgnp', 'tb3m', 'gs10', 'm1sk']]
timeindex = pd.date_range('1959-01', periods = len(usm), freq = 'QS')
usm.index = timeindex
usm.rgnp = np.log(usm.rgnp)
usm.m1sk = np.log(usm.m1sk)
usm.columns = ['lrgnp', 'tb3m', 'gs10', 'lm1sk']
fig = plt.figure()
usm.lrgnp.plot(ax = fig.add_subplot(221))
plt.title('Log of the U.S. real GNP')
usm.lm1sk.plot(ax = fig.add_subplot(222))
plt.title('Log of the U.S. M1 money stock')
usm.tb3m.plot(ax = fig.add_subplot(223))
plt.title('Rate of U.S. 3-month treasury bills')
usm.gs10.plot(ax = fig.add_subplot(224))
plt.title('U.S. 10-year constant maturity interest rate')
plt.savefig('pyTSA_MAcroUSCointegration_fig9-37.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
olsres = smf.ols('usm.lm1sk ~ usm.lrgnp', data = usm).fit()
print(olsres.summary())
olsresid = olsres.resid
olsresid.plot()
plt.savefig('pyTSA_MAcroUSCointegration_fig9-38.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
adfuller(olsresid, regression = 'ct')
kpss(olsresid, regression = 'ct', nlags = 'auto')
coint(usm.lrgnp, usm.lm1sk, trend = 'c')
dusm = usm.diff(1).dropna()
dusm.columns = ['dlrgnp', 'dtb3m', 'dgs10', 'dlm1sk']
kpss(dusm.dlrgnp, regression = 'c', nlags = 'auto')
adfuller(dusm.dlrgnp, regression = 'c')
kpss(dusm.dlm1sk, regression = 'c', nlags = 'auto')
adfuller(dusm.dlm1sk, regression = 'c')
olsres2 = smf.ols('dusm.dlm1sk ~ dusm.dlrgnp', data = dusm).fit()
print(olsres2.summary())