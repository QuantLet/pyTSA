import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv('Yearly mean total sunspot number 1700 - 2017.csv',  delimiter = ';', header = None) 
x.index = x[0];
sunspot = x.drop(columns=[0, 2, 3, 4])
sunspot.plot(legend = False, color="green"); plt.title('Yearly mean total sunspot number')
plt.ylabel('Sunspot number'); plt.xlabel('Year'); plt.show()
plt.savefig('Sunspot_number.png')