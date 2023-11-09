import math
import matplotlib.pyplot as plt


def geometry_distribution(p, attempts):
    return (1 - p) ** (attempts - 1) * p


def binomial_distribution(p, num_item, choose_tims):
    return math.comb(num_item, choose_tims) * (p ** choose_tims) * ((1 - p) ** (num_item - choose_tims))


def draw_binomial_graph(probability, num_tims):
    result = []
    for i in range(num_tims):
        result.append(binomial_distribution(probability, num_tims, i))
    plt.plot(result, label='binomial graph')
    plt.xlabel(f'succeed x time out of {num_tims} attempts')
    plt.ylabel(f'probability {probability} in {num_tims} tims')
    plt.legend()
    plt.show()




if __name__ == '__main__':
    draw_binomial_graph(0.5, 10)
