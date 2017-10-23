#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:49:39 2017

@author: Cling
"""

import re
import random

__all__ = ['L_System']


class L_System:
    axiom = None
    rules = None

    def __init__(self, axiom=None, rules=None):
        self.axiom = axiom
        self.string = self.axiom
        self.generation = 0
        self.rules = rules

    @staticmethod
    def _str_multi_replace(string, dict_replace_table):
        re_replace_table = re.compile(
            '|'.join(map(re.escape, dict_replace_table))
        )

        return re_replace_table.sub(
            lambda match: dict_replace_table[match.group(0)], string
        )

    def step(self):
        self.string = self._str_multi_replace(self.string, self.rules)
        self.generation += 1

    def evaluate(self, depth):
        for i in range(depth):
            self.step()

    def reset(self):
        self.generation = 0
        self.string = self.axiom

    def __getitem__(self, index):
        return self.string[index]

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def __repr__(self):
        return '%s(axiom=\'%s\', rules={%s}) at generation %d = \'%s\'' % (
            self.__class__.__name__,
            self.axiom,
            ', '.join(['\'%s\':\'%s\'' % x for x in self.rules.items()]),
            self.generation,
            self.string
        )


class Random_L_System(L_System):
    '''
    lsys_random = Random_L_System(
        axiom='FX',
        rules={"X": [[0.5, "X+YF+"],[0.5, "Y+X+"]], "Y": "-FX-Y"}
    )
    lsys_random.evaluate(10)
    '''
    @staticmethod
    def _b_is_listlike_iter(obj):
        return hasattr(obj, '__iter__') and not isinstance(obj, (str, dict))

    def step(self):
        # generate string replace dict using L_System rules
        dict_replace_table = {}
        for k, v in self.rules.items():
            if self._b_is_listlike_iter(v):
                n_rand_val = random.random()
                n_prob_sum = 0
                n_idx = 0
                for n_idx, item in enumerate(v):
                    n_prob_sum += item[0]
                    if n_rand_val < n_prob_sum:
                        break
                dict_replace_table[k] = v[n_idx][1]
            else:
                dict_replace_table[k] = v

        self.string = self._str_multi_replace(self.string, dict_replace_table)
        self.generation += 1
