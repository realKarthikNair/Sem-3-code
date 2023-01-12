"""Write a  python program to create a  plotting of years of compounding v/s value of principal using the pyplot library. Assume reasonable values for principal, interest rate, and years.
"""

import matplotlib.pyplot as plt

def plot_compounding(principal, interest_rate, years):
    x = list(range(years + 1))
    y = [principal * (1 + interest_rate) ** i for i in x]
    plt.plot(x, y)
    plt.xlabel('Years')
    plt.ylabel('Value of Principal')
    plt.title('Value of Principal over Time')
    plt.show()
    
plot_compounding(1000, 0.05, 10)
