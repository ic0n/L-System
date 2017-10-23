#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
testing my random select method see if it's random enough
'''
import random

def random_select(lst):
    n_rand_val = random.random()
    n_prob_sum = 0
    n_idx = 0
    for n_idx, item in enumerate(lst):
        n_prob_sum += item[0]
        if n_rand_val < n_prob_sum:
            break
    return lst[n_idx][1]

def main():
    test_set = [
        [1/2, 1],
        [1/4, 2],
        [1/4, 3]
    ]

    case_counter = []
    for i in range(len(test_set)):
        case_counter.append(0)

    for i in range(400000):
        result = random_select(test_set)
        for idx, item in enumerate(test_set):
            if result == item[1]:
                case_counter[idx] += 1
                break

    for idx, item in enumerate(case_counter):
        print("Case {}: {}".format(idx, item))

if __name__ == '__main__':
    main()
