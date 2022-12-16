import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
t = np.arange(500)
f_t = 0.2 + 0.1 * t
f_t = pd.Series(f_t)
p_t = 2 * np.sin(2 * np.pi * t/50  + 0.3 * np.pi)
p_t = pd.Series(p_t)
np.random.seed(1357)
x_n = np.random.normal(loc = 0, scale = 4.2, size = 500)
x_n = pd.Series(x_n)
fx_n = f_t + x_n; fx = f_t * x_n
px_n = p_t + x_n; px = p_t * x_n
fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
fx_n.plot(ax = fig.add_subplot(411))
plt.title('$0.2 + 0.1t$ + N(0,$4.2ˆ2$)')
fx.plot(ax = fig.add_subplot(412))
plt.title('($0.2 + 0.1t$)N(0,$4.2ˆ2$)')
px_n.plot(ax = fig.add_subplot(413))
plt.title('$ 2\sin(2\pi t/50 + 0.3\pi)$ + N(0,$4.2ˆ2$)')
px.plot(ax = fig.add_subplot(414))
plt.title('$ 2\sin(2\pi t/50  + 0.3\pi)$ N(0,$4.2ˆ2$)')
fig.tight_layout(pad = 1.5)
plt.xlabel('Time'); 
plt.savefig('pyTSA_TSComposition_fig2-10.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True);
plt.show()
fApAx = f_t + p_t + x_n
fAp_x = (f_t + p_t) * x_n
fAx_p = (f_t + x_n) * p_t
pAx_f = (p_t + x_n) * f_t
fig = plt.figure()
fig.set_size_inches(18.5, 10.5)
fApAx.plot(ax = fig.add_subplot(411))
plt.title('$0.2 + 0.1t + 2\sin(2\pi t/50  + 0.3\pi)$ + N(0,$4.2ˆ2$)')
fAp_x.plot(ax = fig.add_subplot(412))
plt.title('($0.2 + 0.1t + 2\sin(2\pi t/50 + 0.3\pi)$)N(0,$4.2ˆ2$)')
fAx_p.plot(ax = fig.add_subplot(413))
plt.title('($0.2 + 0.1t$ + N(0,$4.2ˆ2$))$2\sin(2\pi t/50 + 0.3\pi)$)')
pAx_f.plot(ax = fig.add_subplot(414))
plt.title('($2\sin(2\pi t/50 + 0.3\pi)$ + N(0,$4.2ˆ2$))($0.2 + 0.1t$)')
fig.tight_layout(pad = 1.5)
plt.xlabel('Time'); 
plt.savefig('pyTSA_TSComposition_fig2-11.png', dpi = 1200, 
             bbox_inches ='tight', transparent = True);
plt.show()