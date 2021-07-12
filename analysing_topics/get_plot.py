import matplotlib
matplotlib.use('Agg')
import numpy as np
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

# 00:06.503 00:11.384 hello p
# 00:11.634 06:36.084 meeting-fu p
# 01:16.376 01:45.281 transport s
# 06:38.965 06:43.727 operator p
def main():

    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()
    x = np.linspace(0, 10, 1000)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.sin(x - 0), color='blue')
    plt.plot(x, np.sin(x - 1), color='g')
    plt.plot(x, np.sin(x - 5), color='chartreuse')
    plt.plot(x, x + 0, linestyle='solid')
    plt.plot(x, x + 1, linestyle='dashed')
    plt.plot(x, x + 2, linestyle='dashdot')
    plt.plot(x, x + 3, linestyle='dotted')
    # plt.xlim(-1, 410)
    # plt.ylim(0, 4.5)
    plt.title("A Sine Curve")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    fig.savefig("tmp.png")

if __name__ == "__main__":
    main()
