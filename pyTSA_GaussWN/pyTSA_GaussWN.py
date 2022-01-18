from numpy import random
import pandas as pd
random.seed(135) # for repeat
x=random.normal(loc=0, scale=1, size=1000)
xts=pd.Series(x)
import matplotlib.pyplot as plt
xts.plot(); plt.xlabel('Time')
plt.ylabel('Simulated white noise'); plt.show()
from PythonTsa.plot_acf_pacf import acf_pacf_fig
acf_pacf_fig(xts, both=False, lag=30)