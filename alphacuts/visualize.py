#!/usr/bin/python2.7
__author__ = 'tsabsch <tim@sabsch.com>'

import bisect
import matplotlib.pyplot as plt

def horizontal_view(alpha_cuts):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot each alpha cut range in the dict
    for degree, alpha_cut in alpha_cuts.iteritems():
        for iv in acut:
            ax.plot(iv, [degree,degree], marker='.', color='black')

    # set y axis to interval [0,1]
    ax.set_ylim([0,1.1])
    ax.set_yticks(alpha_cuts.keys())

    return fig

def upper_envelope(alpha_cuts):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    xs = list()
    ys = list()
    tmp_steps = list()

    for degree, cuts in alpha_cuts.iteritems():

        # insert temporary steps
        for x in tmp_steps:
            i = bisect.bisect_left(xs, x)
            xs.insert(i, x)
            ys.insert(i, degree)
        tmp_steps = list()

        for (start, end) in cuts:
            if end not in xs:
                # insert new (down) step
                i = bisect.bisect(xs, end)
                xs.insert(i, end)
                ys.insert(i, degree)

            if start in xs:
                if start == end:
                    # special case: peak
                    tmp_steps += [start]
                else:
                    # update step
                    i = xs.index(start)
                    ys[i] = degree
            else:
                # new up step detected, put on hold until degree is determined
                tmp_steps += [start]

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.step(xs,ys)
    ax.set_ylim([0,1.1])
    ax.set_yticks(alpha_cuts.keys())
    return fig

def visualize(alpha_cuts, kind='horizontal_view'):
    plt.ion()
    if kind == 'horizontal_view':
        fig = horizontal_view(alpha_cuts)
    if kind == 'upper_envelope':
        fig = upper_envelope(alpha_cuts)

    return fig

def init_handler(fig):
    ax = fig.gca()
    line, = ax.plot([],[])
    default_xticks = ax.xaxis.get_majorticklocs().tolist()
    return line, default_xticks

def visualize_x(fig, line, default_xticks, x, y):
    ax = fig.gca()


    # update vertical line
    line.set_xdata([x,x])
    line.set_ydata([0,y])
    line.set_color('red')

    # update xticks
    ax.set_xticks(default_xticks + [x])

    return line
