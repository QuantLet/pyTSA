import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig
x = pd.read_csv('gdpquarterlychina1992.1-2017.4.csv', header = 0) 
dates = pd.date_range(start='1992', periods = len(x), freq='Q')
x.index = dates
x.plot(); plt.title('Chinese Quarterly GDP 1992 2017')
plt.ylabel('billions of RMB'); plt.show()
acf_pacf_fig(x, both = False, lag = 60)