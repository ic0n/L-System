#!/usr/bin/env python3
# -*- coding: utf-8 -*-"""

"""
Created on Mon Apr 24 15:59:19 2017

@author: Cling
"""


import lsystem
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections


def a_calculate_lines(
        string, n_angle=90, n_line_len=2, t_init_pos=(0.0, 0.0), n_init_dir=0,
        n_draw_step_scale=1
):
    a_pen_pos = np.array(t_init_pos)
    n_direction = np.deg2rad(n_init_dir)
    n_rot_angle = np.deg2rad(n_angle)
    n_draw_len = n_line_len
    lst_lines = []
    lst_stack = []
    lst_line_len_stack = []
    for cmd in string:
        if cmd in 'FAB':
            a_pen_pos_nxt = a_pen_pos + n_draw_len *\
                            np.array((
                                np.cos(n_direction),
                                np.sin(n_direction)
                            ))
            lst_lines.append(np.array((a_pen_pos, a_pen_pos_nxt)))
            a_pen_pos = a_pen_pos_nxt
        elif cmd == "+":
            n_direction += n_rot_angle
        elif cmd == "-":
            n_direction -= n_rot_angle
        elif cmd == "(":
            lst_line_len_stack.append(n_draw_len)
            n_draw_len *= n_draw_step_scale
        elif cmd == ")":
            n_draw_len = lst_line_len_stack.pop()
        elif cmd == "[":
            lst_stack.append((a_pen_pos, n_direction))
        elif cmd == "]":
            a_pen_pos, n_direction = lst_stack.pop()
    a_lines = np.array(lst_lines)
    return a_lines


def main():
#    lsys_dragon = lsystem.L_System(
#        axiom='FX',
#        rules={"X": "X+YF+", "Y": "-FX-Y"}
#    )
#    lsys_dragon.evaluate(10)
#
#    a_lines = a_calculate_lines(lsys_dragon, 90)
#
#    lsys_tree = lsystem.Random_L_System(
#        axiom='F',
#        rules={'F': [
#            [1/2, 'F[+F]F[-F]F'],
#            [1/4, 'F[+F]F[-F[+F]]'],
#            [1/4, 'FF[-F+F+F]+[+F-F-F]']
#        ]}
#    )
#    lsys_tree.evaluate(6)
#    print(len(lsys_tree))
#    return None
    lsys_tree = lsystem.L_System(
        axiom='X',
        rules={'X': '(F[+X][-X]FX)'}
    )
    lsys_tree.evaluate(3)
    a_lines = a_calculate_lines(lsys_tree, 27.9, n_init_dir=90, n_draw_step_scale=0.5)
    lines = collections.LineCollection(a_lines)
    ax = plt.axes()
    ax.add_collection(lines)
    ax.axis("equal")
    ax.set_xlim(ax.dataLim.xmin, ax.dataLim.xmax)
    plt.show()

if __name__ == '__main__':
    main()
