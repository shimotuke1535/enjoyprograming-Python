
import numpy as np
import matplotlib.pyplot as plt

scale = 1
optical = 5000000

x = np.linspace(-np.pi*scale, np.pi*scale, optical).reshape(-1, 1)
rand1 = np.random.rand()
rand2 = np.random.rand()
rand3 = np.random.rand()
t = np.sin(rand1*x)-(np.cos(rand2*x-0.1))*np.sin(rand3*x+2)

plt.plot(x, t)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

from keras.models import Sequential
from keras.layers import Dense

batch_size = 2500
n_in = 1
n_mid = 500
n_out = 1
Epoch_val = 100

model = Sequential()
model.add(Dense(n_mid, input_shape = (n_in,), activation = "sigmoid"))
model.add(Dense(n_out, activation = "linear"))
model.compile(loss = "mean_squared_error", optimizer = "sgd")
print(model.summary())

history = model.fit(x, t, batch_size = batch_size, epochs = Epoch_val, validation_split = 0.1)

loss_train = history.history['loss']
loss_val = history.history['val_loss']

plt.plot(np.arange(len(loss_train)), loss_train, label = "loss_train")
plt.plot(np.arange(len(loss_val)), loss_val, label = "loss_val")
plt.legend()
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

plt.plot(x, model.predict(x), label = "f(x)_predict")
plt.plot(x, t, label = "f(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
