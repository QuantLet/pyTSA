import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_absolute_percentage_error
from PythonTsa.plot_acf_pacf import acf_pacf_fig
tsdta = pd.read_csv('elec-temp.csv')
tsdta['time'] = pd.to_datetime(tsdta['time'])
tsdta.index = tsdta['time']
loadts = tsdta.drop(columns = ['time', 'temp'])
len(loadts)
loadts1 = loadts[loadts.index < '2012-01-14 23:00:00']
loadts1.plot()
plt.savefig('pyTSA_ML_fig10-3.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
loadts2 = loadts[loadts.index >'2014-12-18 00:00:00']
loadts2.plot()
plt.savefig('pyTSA_ML_fig10-4.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
loadts3 = loadts[(loadts.index > '2012-03-01 00:00:00')&(loadts.index < '2014-03-01 00:00:00')]
loadts3.plot()
plt.savefig('pyTSA_ML_fig10-5.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
loadts4 = loadts[loadts.index <= '2013-12-31 23:00:00']
loadts4.plot()
plt.savefig('pyTSA_ML_fig10-6.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
validtime = '2014-09-01 00:00:00'
testtime = '2014-11-01 00:00:00'
loadts[loadts.index <validtime].rename(columns = {'load':'train'}).join(loadts[(loadts.index >= validtime)&(loadts.index < testtime)].rename(columns
 = {'load':'validation'}), how = 'outer').join(loadts[testtime:].rename(columns = {'load':'test'}), how = 'outer').plot(y = ['train', 'validation', 'test'], style = ['-', '-.', '--'])
plt.ylabel('Electricity load')
plt.savefig('pyTSA_ML_fig10-7.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
train = loadts.copy()[loadts.index < validtime]
valid = loadts.copy()[(loadts.index >= validtime)&(loadts.index < testtime)]
test = loadts.copy()[loadts.index >= testtime]
scaler = MinMaxScaler()
train['load'] = scaler.fit_transform(train)
valid['load'] = scaler.fit_transform(valid)
test['load'] = scaler.fit_transform(test)
acf_pacf_fig(train.load, lag = 72)
plt.savefig('pyTSA_ML_fig10-8.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
T = 24
# Let the input be a vector of the previous 24 hours of the load values.
HORIZON = 1 # one-step-ahead prediction
train_shifted = train.copy()
train_shifted['y_t+1'] = train_shifted['load'].shift(-1, freq = 'H')
for t in range(1, T+1):
	train_shifted[str(T-t)] = train_shifted['load'].shift(T-t, freq = 'H')
y_col = 'y_t+1'
X_cols = ['load_t-23', 'load_t-22', 'load_t-21', 'load_t-20', 
		 'load_t-19', 'load_t-18', 'load_t-17', 'load_t-16', 
		 'load_t-15', 'load_t-14', 'load_t-13', 'load_t-12', 
		 'load_t-11', 'load_t-10', 'load_t-9', 'load_t-8', 
		 'load_t-7', 'load_t-6', 'load_t-5', 'load_t-4', 
		 'load_t-3', 'load_t-2', 'load_t-1', 'load_t']
train_shifted.columns = ['load_original'] + [y_col] + X_cols
train_shifted = train_shifted.dropna(how = 'any')
y_train = np.array(train_shifted[y_col]) # equal to y_train = train_shifted[y_col].to_numpy()
X_train = np.array(train_shifted[X_cols])
X_train = X_train.reshape(X_train.shape[0], T, 1)
valid_shifted = valid.copy()
test_shifted = test.copy()
valid_shifted['y_t+1'] = valid_shifted['load'].shift(-1, freq = 'H')
test_shifted['y_t+1'] = test_shifted['load'].shift(-1, freq = 'H')
for t in range(1, T+1):
	valid_shifted[str(T-t)] = valid_shifted['load'].shift(T-t, freq = 'H')
for t in range(1, T+1):
	test_shifted[str(T-t)] = test_shifted['load'].shift(T-t, freq = 'H')
valid_shifted.columns = ['load_original'] + [y_col] + X_cols
test_shifted.columns = ['load_original'] + [y_col] + X_cols
valid_shifted = valid_shifted.dropna(how = 'any')
test_shifted = test_shifted.dropna(how = 'any')
y_valid = np.array(valid_shifted[y_col])
y_test = np.array(test_shifted[y_col])
X_valid = np.array(valid_shifted[X_cols])
X_test = np.array(test_shifted[X_cols])
X_valid = X_valid.reshape(X_valid.shape[0], T, 1)
X_test = X_test.reshape(X_test.shape[0], T, 1)
latent_dim = 6
batch_size = 32
epochs = 15
model = Sequential()
model.add(GRU(latent_dim, input_shape = (T, 1)))
model.add(Dense(HORIZON))
model.compile(optimizer = 'RMSprop', loss = 'mse')
model.summary()
GRU_earlystop = EarlyStopping(monitor = 'val_loss', min_delta = 0, patience = 5) 
model_fit = model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs, validation_data = (X_valid, y_valid), callbacks = [GRU_earlystop], verbose = 1)
preds = model.predict(X_test)
evdta = pd.DataFrame(preds, columns = ['t+' + str(t)
        for t in range(1, HORIZON + 1)])
evdta['time'] = test_shifted.index
evdta = pd.melt(evdta, id_vars = 'time', 
value_name = 'fitted', var_name = 'h')
evdta['actual'] = np.transpose(y_test).ravel()
evdta[['fitted', 'actual']] = scaler.inverse_transform(evdta[['fitted', 'actual']])
evdta.head()
mean_absolute_percentage_error(evdta['actual'], evdta['fitted'])
evdta[evdta.time<'2014-11-08'].plot(x = 'time', 
y = ['fitted', 'actual'], style = ['--r', '-b'])
plt.ylabel('Electricity load')
plt.savefig('pyTSA_ML_fig10-9.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()
resid = evdta['actual']-evdta['fitted']
acf_pacf_fig(resid, lag = 72)
plt.savefig('pyTSA_ML_fig10-10.png', dpi = 1200, bbox_inches ='tight', 
            transparent = True, legend = None); plt.show()