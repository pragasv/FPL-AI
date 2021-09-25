import matplotlib.pyplot as plt

from src.visualizer.utils import draw_pitch, draw_half_pitch


X_CORD_FORWARD = [65, 65, 65]
Y_CORD_FORWARD = [20, 40, 60]

X_CORD_MIDFIELD = [85, 85, 85, 85, 85, 85]
Y_CORD_MIDFIELD = [10, 20, 35, 45, 60, 70]

X_CORD_DEFENCE = [100, 100, 100, 100, 100, 100]
Y_CORD_DEFENCE = [10, 20, 35, 45, 60, 70]

X_CORD_KEEP = [115, 115]
Y_CORD_KEEP = [35, 45]


def pitch_view(forwards, midfields, defenders, keepers):
    """
    :param forwards: forward player names
    :param midfields: midfield player names
    :param defenders: defend player names
    :param keepers: goalkeeper player names
    :return: N/A
    """
    fig=plt.figure()
    fig.set_size_inches(10, 8)
    ax=fig.add_subplot(1, 1, 1)
    draw_half_pitch(ax)

    for i in range(len(forwards)):
        plt.text(X_CORD_FORWARD[i] + .03, Y_CORD_FORWARD[i] + .03, forwards[i], fontsize=7)

    for i in range(len(midfields)):
        plt.text(X_CORD_MIDFIELD[i] + .03, Y_CORD_MIDFIELD[i] + .03, midfields[i], fontsize=7)

    for i in range(len(defenders)):
        plt.text(X_CORD_DEFENCE[i] + .03, Y_CORD_DEFENCE[i] + .03, defenders[i], fontsize=7)

    for i in range(len(keepers)):
        plt.text(X_CORD_KEEP[i] + .05, Y_CORD_KEEP[i] + .03, keepers[i], fontsize=7)

    ax.scatter(X_CORD_FORWARD, Y_CORD_FORWARD, c='red', label='forwards')
    ax.scatter(X_CORD_MIDFIELD, Y_CORD_MIDFIELD, c='blue', label='midfielders')
    ax.scatter(X_CORD_DEFENCE, Y_CORD_DEFENCE, c='green', label='defenders')
    ax.scatter(X_CORD_KEEP, Y_CORD_KEEP, c='black', label='keepers')

    plt.ylim(0, 80)
    plt.xlim(60, 120)
    plt.legend(loc='upper left')
    plt.show()