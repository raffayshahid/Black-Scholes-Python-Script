import numpy as np
from scipy.stats import norm


# define variables
r = 0.01 # risk free rate
S = 39 # initial price
K = 48 # strike price
T=240/365 # time to maturity
sigma = 0.30 # volatility


def blackScholes(r, S, K, T, sigma, type="C"):
    d1 = (np.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1-sigma*np.sqrt(T)
    if type == "C":
        return S*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)
    elif type == "P":
        return K*np.exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
    else:
        print("Invalid type")
        return None



print ("Option Price is: ", blackScholes(r, S, K, T, sigma, "C"))