import numpy as np

n_samples = 300
noise = 0.1

X = np.random.uniform(-3, 3, size=(n_samples, 2))
np.random.shuffle(X)

y1 = np.sin(X[:, 0]) + X[:, 1]
y2 = np.cos(X[:, 1]) - X[:, 0]
y3 = X[:, 0] * X[:, 1]

Y = np.vstack((y1, y2, y3)).T + np.random.normal(0, noise, size=(n_samples, 3))

data_set = np.hstack((X, Y))

train, validation, test = np.split(data_set, [int(0.35*n_samples), int(0.7*n_samples)], axis=0)

train_mu = np.mean(train, axis=0)
train_sigma = np.std(train, axis=0)

train = (train - train_mu) / train_sigma
validation = (validation - train_mu) / train_sigma
test = (test - train_mu) / train_sigma

x_train, x_validation, x_test = train[:, :2], validation[:, :2], test[:, :2]
y_train, y_validation, y_test = train[:, 2:], validation[:, 2:], test[:, 2:]
