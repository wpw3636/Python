from scipy.stats import norm

def zscore(mu,sigma,tail,z):
    if tail == "left":
        p = norm.cdf(z,mu,sigma)
        return p
    elif tail == "right":
        p = 1 - norm.cdf(z,mu,sigma)
        return p
    else:
        return "Enter valid tail"
    
mu = 100
sigma = 15
tail = "right"
z = 100

print(zscore(mu,sigma,tail,z))