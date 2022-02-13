import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_acf_pacf import acf_pacf_fig

x = pd.read_csv('gdpquarterlychina1992.1-2017.4.csv', header = 0) 
dates = pd.date_range(start='1992', periods = len(x), freq='Q')
acf_pacf_fig(x, both = False, lag = 60); plt.savefig('pyTSA_GDPChina_Fig1-8.png', 
                                                     transparent = True, dpi = 1200, )
x.index = dates
x.plot(legend = None); plt.title('Chinese Quarterly GDP 1992 2017'); 
plt.ylabel('billions of RMB'); plt.xlabel('Years'); 
plt.savefig('pyTSA_GDPChina_Fig1-7.png', dpi = 1200, bbox_inches='tight',
                                           transparent = True);