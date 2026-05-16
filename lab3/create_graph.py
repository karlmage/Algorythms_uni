import matplotlib.pyplot as plt
from math import log10

def draw_graph(x_vals: list, y_vals: list,      #y_vals = [[y], [y], ...]
               x_label: str = "x", y_label: str = "y"):
    for y in y_vals:
        plt.plot(x_vals, y)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    return 0

def draw_error_graph(x_vals: list, y_vals: list):
    neg_log_d_n_list = []
    for y in y_vals:
        neg_log_d_n = []
        for y_item in y:
            if y_item == 0:
                neg_log_d_n.append(0)
            else:
                neg_log_d_n.append(log10(abs(y_item)))
        neg_log_d_n = [i * (-1) for i in neg_log_d_n]
        neg_log_d_n_list.append(neg_log_d_n)
    return draw_graph(x_vals, neg_log_d_n_list, x_label="x\'", y_label="-lg(delta n)")