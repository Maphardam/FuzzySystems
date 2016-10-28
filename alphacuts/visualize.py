#!/usr/bin/python2.7
__author__ = 'tsabsch <tim@sabsch.com>'

import matplotlib.pyplot as plt

def plot(acuts):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot each alpha cut range in the dict
    for mship, acut in acuts.iteritems():
        for iv in acut:
            ax.plot(iv, [mship,mship], marker='.', color='black')

    # set y axis to interval [0,1]
    ax.set_ylim([0,1.1])
    ax.set_yticks(acuts.keys())

    return fig

def visualize(acuts, type='simple'):
    if type == 'simple':
        fig = plot(acuts)
    if type == 'upper_envelope':
        raise NotImplementedError()

    plt.show()