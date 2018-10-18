# Replication of the bayesian generalization
# model found in
# Tenenbaum & Griffiths (2001)
# Generalization, similarity, and Bayesian inference.
# Behavioral and Brain Sciences, 24, 629-640.

import numpy as np
import math
import matplotlib.pyplot as plt
import sys

def createModel(hypo_size_max=6, y_interval=[38, 52], x_examples=[45]):
    print(hypo_size_max, y_interval, x_examples)
    # possible y
    step_size = 1 #integers
    start = y_interval[0]
    end_inclu = y_interval[1]
    poss_y = np.arange(start, end_inclu + 1, step_size)
    #initialize the distribution
    prob_y_in_C = dict(zip(poss_y, [0] * (y_interval[1] - y_interval[0] + 1)))
    prob_y_in_C_empty = prob_y_in_C.copy()

    prior = 1 #uniform, p(h), dont really need to use
    #print(poss_y)
    size_of_X = len(x_examples)

    for y in poss_y:
        prob_h_given_x_i = prob_y_in_C_empty.copy()
        for hypo_size in range(1, hypo_size_max+1):
            curr_hypo = list(range(y, y+hypo_size))
            #print(curr_hypo)
            add_it = 1
            for x_i in x_examples:
                if x_i not in curr_hypo:
                    add_it = 0
                    break
            if add_it == 1:
                #print(curr_hypo)
                for i in curr_hypo:
                    if i >= start and i <= end_inclu:
                        prob_h_given_x_i[i] += 1
                for key in prob_h_given_x_i:
                    prob_y_in_C[key] += prob_h_given_x_i[key]

    #print(prob_y_in_C)
    prob_y_in_C = normalize(prob_y_in_C)
    x_values = list(prob_y_in_C.keys())
    y_values = list(prob_y_in_C.values())
    plt.plot(x_values, y_values, linewidth='1', color='#333333')
    for x in x_examples:
        plt.plot(x, 0, marker='.', color="#333333")
    plt.xticks(list(range( start, end_inclu+10, int((end_inclu-start)/10) ) ) )
    plt.yticks([0,1])
    plt.ylabel("p(y ∈ C | X)")
    plt.margins(0,0.02)
    plt.show()
    return 1

def normalize(l):
    x_values = list(l.keys())
    y_values = list(l.values())
    alp = max(y_values)
    y_values_norm = [val/alp for val in y_values]
    return dict(zip(x_values, y_values_norm))

if __name__ == "__main__":
    args = sys.argv[1:]
    hypo_size_max = int(args[0])
    y_interval = [int(args[1]), int(args[2])]
    x_examples = []
    for i in range(3, len(args)):
        x_examples.append(int(args[i]))
    createModel(hypo_size_max, y_interval, x_examples)
