from PythonTsa.True_acf import Tacf_pacf_fig
ar = [1, -0.8, 0.6]
ma = [1, 0.7, 0.4]
Tacf_pacf_fig(ar, ma, both = True, lag = 20)