import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
milk = pd.read_excel('milk.xlsx', header = None)
type(milk)
milk
mseries = pd.concat([milk.loc[0], milk.loc[1], milk.loc[2], 
milk.loc[3], milk.loc[4], milk.loc[5], milk.loc[6], 
milk.loc[7], milk.loc[8], milk.loc[9], milk.loc[10], 
milk.loc[11], milk.loc[12], milk.loc[13], milk.loc[14],
milk.loc[15], milk.loc[16]], ignore_index = 'true')
type(mseries)
mts = mseries.drop([168,169])
mts
timeindex = pd.date_range('1962 01',periods = 168,freq = 'M')
mts.index = timeindex
mts
mts.plot()
plt.title('Milk Average per Cow from Jan.1962 to Dec.1975')
plt.xlabel('Time'); plt.ylabel('Milk Average'); 
plt.savefig('pyTSA_MilkAv_Fig1-2.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
my = np.array(mts).reshape(14,12)
myt = np.transpose(my)
year = [1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969,
1970, 1971,1972, 1973, 1974, 1975]
myt = pd.DataFrame(myt, columns = year)
bp = myt.boxplot()
plt.xlabel('Year'); plt.ylabel('Milk Average'); 
plt.xticks(rotation = 45, ha = 'right')
plt.savefig('pyTSA_MilkAv_Fig1-19.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
'Aug', 'Sep', 'Oct', 'Nov','Dec']
myd = pd.DataFrame(my, columns = month)
bpm = myd.boxplot()
plt.xlabel('Month'); plt.ylabel('Milk Average'); 
plt.savefig('pyTSA_MilkAv_Fig1-20.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True, legend = None); plt.show()