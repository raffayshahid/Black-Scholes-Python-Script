# define variables
r = 0.01 # risk free rate
s = 0.2 # volatility
T = 1.0 # time to maturity
K = 100.0 # strike price
S0 = 100.0 # initial price
N = 100 # number of steps
dt = T/N # time step





# define functions
s = 39
K = 48
T=240/365
sigma = 0.30
def blackScholes(r, S, K, T,
sigma,
type-"C*b:
"Calculate BS option price for a call/put"
d1 = (np.log(s/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt (T))
d2 = d1 - sigma*np.sqrt(T)
try:
if type
"C"
price = S*norm.cdf(d1, 0, 1)
- K*np.exp(-r*T)*norm.cdf(d2, 8, 1)
elif type ==
"p".
price = K*np.exp(-r*T)*norm.cdf(-d2, 8, 1)
- S*norm.cdf(-d1, 0, 1)
return price
except:
print ("Please confirm all option parameters above!!!")
print ("Option Price is: