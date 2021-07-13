import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def main():
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()

    # plotting horizontal lines with labels and colors
    ax.hlines(y=1, xmin=6, xmax=11, label='hello', linewidth=2, color='blue')
    ax.hlines(y=2, xmin=11, xmax=396, label='meeting', linewidth=2, color='orange')
    ax.hlines(y=3, xmin=76, xmax=105, label='transport', linewidth=2, color='green')
    ax.hlines(y=4, xmin=398, xmax=403, label='operator', linewidth=2, color='red')
    ax.autoscale()
    ax.margins(0.1)

    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # adding title, names to x-axis, y-axis, legends, image name
    plt.title('test')
    plt.xlabel('Seconds')
    plt.ylabel('Topic ID')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    fig.savefig('test.png')
    return 0


if __name__ == "__main__":
    main()
# plt.legend(loc='upper left')
# fig = plt.figure()
# x = np.array([0,1,2,3])
# y = np.array([0.650, 0.660, 0.675, 0.685])
# my_xticks = ['a', 'b', 'c', 'd']
# plt.xticks(x, my_xticks)
# plt.yticks(np.arange(y.min(), y.max(), 0.005))
# plt.plot(x, y)
# plt.grid(axis='y', linestyle='-')
# fig.savefig("tmp.png")
# plt.plot(x, y_1, marker='x')
# plt.plot(x, y_2, marker='^')
# plt.plot(x, np.sin(x))
# plt.plot(x, np.sin(x - 0), color='blue')
# plt.plot(x, np.sin(x - 1), color='g')
# plt.plot(x, np.sin(x - 5), color='chartreuse')
# plt.plot(x, x + 0, linestyle='solid')
# plt.plot(x, x + 1, linestyle='dashed')
# plt.plot(x, x + 2, linestyle='dashdot')
# plt.plot(x, x + 3, linestyle='dotted')
# plt.title("A Sine Curve")
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# fig.savefig("tmp.png")