from math import sqrt, pi, exp


def gaussian(mean, variavce, x):
    return 1 / sqrt(2. * pi * variavce) * exp(-.5 * (x - mean) ** 2 / variavce)


def update(mean1, var1, mean2, var2):
    # Combination of prior and measurement probability
    # Function calculates new mean and variance of combined gaussian distribution
    mean3 = (var1 * mean2 + var2 * mean1) / (var1 + var2)
    var3 = 1 / (1 / var1 + 1 / var2)
    return [mean3, var3]


def predict(mean1, var1, mean2, var2):
    # predict the new mean and variance given the mean and variance of
    # prior belief and the mean and variance of motion
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range (len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)
    
print(mu,sig)
