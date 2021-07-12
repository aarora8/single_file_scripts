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

    # plt.style.use('seaborn-whitegrid')
    # fig = plt.figure()
    # ax = plt.axes()
    # x = np.linspace(0, 10, 1000)

    # x = [1, 2, 3]
    # y_1 = [50, 60, 70]
    # y_2 = [20, 30, 40]
    # plt.plot(x, y_1, marker='x')
    # plt.plot(x, y_2, marker='^')
    # # plt.plot(x, np.sin(x))
    # # plt.plot(x, np.sin(x - 0), color='blue')
    # # plt.plot(x, np.sin(x - 1), color='g')
    # # plt.plot(x, np.sin(x - 5), color='chartreuse')
    # # plt.plot(x, x + 0, linestyle='solid')
    # # plt.plot(x, x + 1, linestyle='dashed')
    # # plt.plot(x, x + 2, linestyle='dashdot')
    # # plt.plot(x, x + 3, linestyle='dotted')
    # plt.title("A Sine Curve")
    # plt.xlabel("x")
    # plt.ylabel("sin(x)")
    # fig.savefig("tmp.png")
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    x = np.array([0,1,2,3])
    y = np.array([0.650, 0.660, 0.675, 0.685])
    my_xticks = ['a', 'b', 'c', 'd']
    plt.xticks(x, my_xticks)
    plt.yticks(np.arange(y.min(), y.max(), 0.005))
    plt.plot(x, y)
    plt.grid(axis='y', linestyle='-')
    fig.savefig("tmp.png")

if __name__ == "__main__":
    main()
