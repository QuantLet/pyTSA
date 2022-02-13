import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_process import arma_generate_sample
from PythonTsa.plot_acf_pacf import acf_pacf_fig
from PythonTsa.Selecting_arma import choose_arma
from statsmodels.tsa.arima_model import ARMA
from PythonTsa.LjungBoxtest import plot_LB_pvalue
from scipy import stats
ar = np.array([1, -0.8, 0.6])
ma = np.array([1, 0.7, 0.4])
arma_process = sm.tsa.ArmaProcess(ar, ma)
arma_process.isstationary  # check stationarity
arma_process.isinvertible  # check invertibility
np.random.seed(12357)
y = arma_generate_sample(ar = ar, ma = ma, nsample = 500)
y = pd.Series(y)
# It is always a good idea to make the data a Series!
y.plot(); plt.show()
acf_pacf_fig(y, both = True, lag = 20)
choose_arma(y, max_p = 6, max_q = 7, ctrl = 1.02)
inf = sm.tsa.arma_order_select_ic(y, max_ar = 6, max_ma = 7,
                     ic = ['aic', 'bic', 'hqic'], trend = 'nc')
inf.aic_min_order
inf.bic_min_order
inf.hqic_min_order
arma22 = ARMA(y, order = (2,2)).fit(trend = "nc")
print(arma22.summary())
resid22 = arma22.resid
acf_pacf_fig(resid22, both = True, lag = 20)
plot_LB_pvalue(resid22, noestimatedcoef = 4, nolags = 26)
stats.normaltest(resid22)
#NormaltestResult(statistic = 0.48049991217901883,
 #                pvalue = 0.786431263213941)
arma22.plot_predict(start = 450, end = 509)
plt.show()