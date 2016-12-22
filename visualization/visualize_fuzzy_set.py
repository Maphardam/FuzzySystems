#!/usr/bin/python2.7
__author__ = 'tsabsch <tim@sabsch.com>'

import bisect
import matplotlib.pyplot as plt

def horizontal_view(ax, fuzzy_set):
    # plot each alpha cut range in the dict
    for degree, alpha_cut in fuzzy_set.iter_alphacuts():
        for iv in alpha_cut:
            ax.plot(iv, [degree,degree], marker='.', color='black')

    # set y axis to interval [0,1.1]
    ax.set_ylim([0,1.1])
    ax.set_yticks(fuzzy_set.degrees())

    ax.set_title("Horizontal View")

    return ax

def upper_envelope(ax, fuzzy_set):
    xs = list()
    ys = list()
    tmp_starts = list()

    for degree, cuts in fuzzy_set.iter_alphacuts():
        for (start, end) in cuts:
            if end not in xs:
                # insert new (down) step
                i = bisect.bisect(xs, end)
                xs.insert(i, end)
                ys.insert(i, degree)

            for s in [s for s in tmp_starts if start <= s <= end]:
                # insert new (up) step
                i = bisect.bisect_left(xs, s)
                xs.insert(i, s)
                ys.insert(i, degree)

                tmp_starts.remove(s)

            # plot.step needs the y-value until the start value. as we're going
            # down, this is not known yet. start values are therefore added to
            # a temporary list
            tmp_starts.append(start)

    for s in tmp_starts:
        # flush remaining start points
        i = bisect.bisect_left(xs, s)
        xs.insert(i, s)
        ys.insert(i, 0)

        tmp_starts.remove(s)

    # set y axis to interval [0,1.1]
    ax.step(xs,ys)
    ax.set_ylim([0,1.1])
    ax.set_yticks(fuzzy_set.degrees())
    ax.set_title("Upper Envelope")

    return ax

def visualize(fuzzy_set, kind='both'):
    plt.ion()
    plt.xkcd()
    fig = plt.figure()

    if kind == 'horizontal_view':
        ax = fig.add_subplot(111)
        horizontal_view(ax, fuzzy_set)
    if kind == 'upper_envelope':
        ax = fig.add_subplot(111)
        upper_envelope(ax, fuzzy_set)
    if kind == 'both':
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        horizontal_view(ax1, fuzzy_set)
        upper_envelope(ax2, fuzzy_set)

    fig.canvas.set_window_title("Alpha-Cut Master")

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
