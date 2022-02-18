import pandas as pd
import matplotlib.pyplot as plt
from PythonTsa.SimulSBM import simulSBM
x = simulSBM(seed = 1357, fig = False)
y = simulSBM(seed = 357, fig = False)
z = simulSBM(seed = 3571, fig = False)
# if seed is fixed, the same SBM is reproduced.
# if fig = True, a SBM plot is automatically generated.
xyz = pd.DataFrame({'SBM1': x, 'SBM2': y, 'SBM3': z})
xyz.plot(style = ['-', '--', ':'])
plt.xlabel('Time $t$')
plt.ylabel('Standard Brownian Motion')
plt.savefig('pyTSA_SimSBM_fig9-20.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show() 
