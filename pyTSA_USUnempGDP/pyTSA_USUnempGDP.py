import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.plot_multi_ACF import multi_ACFfig
from PythonTsa.plot_multi_Q_pvalue import MultiQpvalue_plot
mda = pd.read_csv( 'USQgdpunemp.csv', header = 0)
mda = mda[['gdp', 'rate']]
dates = pd.date_range('1948-01', periods = len(mda), freq = 'Q')
mda.index = dates
mda['gdp'] = np.log(mda['gdp'])
mda.columns = ['lgdp', 'rate']
multi_ACFfig(mda, nlags = 16); plt.gcf();
plt.savefig('pyTSA_USUnempGDP_fig7-4.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None)
dmda = mda.diff(1).dropna()
dmda.columns = ['dlgdp', 'drate']
dmda.plot()
plt.savefig('pyTSA_USUnempGDP_fig7-5.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None) ; plt.show()
multi_ACFfig(dmda, nlags = 16);  
plt.savefig('pyTSA_USUnempGDP_fig7-6.png', dpi = 1200, 
            bbox_inches ='tight', transparent = True, legend = None) 
qs, pv = MultiQpvalue_plot(dmda, nolags = 16); 
plt.savefig('pyTSA_USUnempGDP_fig7-7.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None)


