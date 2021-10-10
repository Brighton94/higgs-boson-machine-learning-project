import matplotlib.pyplot as plt
import numpy
import pandas
from sklearn.metrics import roc_curve, roc_auc_score


label_class_correspondence = {'b': 0, 's': 1}
class_label_correspondence = {0: 'b', 1: 's'}


def get_class_ids(labels):
    """
    Convert event types into class ids.

    Parameters:
    -----------
    labels : array_like
        Array of event types ['s', 'b', 'b', ...].

    Return:
    -------
    class ids : array_like
        Array of class ids [1, 0, 0, ...].
    """
    return numpy.array([label_class_correspondence[alabel] for alabel in labels])


def plot_roc_curves(predictions, labels):
    """
    Plot ROC curves.

    Parameters:
    -----------
    predictions : array_like
        Array of particle type predictions with shape=(n_particles, n_types).
    labels : array_like
        Array of class ids [1, 0, 0, ...].
    """
    plt.figure(figsize=(9, 6))
    u_labels = numpy.unique(labels)
    for lab in u_labels:
        y_true = labels == lab
        y_pred = predictions[:, lab]
        fpr, tpr, _ = roc_curve(y_true, y_pred)
        auc = roc_auc_score(y_true, y_pred)
        plt.plot(tpr, 1-fpr, linewidth=3, label=class_label_correspondence[lab] + ', AUC = ' + str(numpy.round(auc, 4)))
        plt.xlabel('Signal efficiency (TPR)', size=15)
        plt.ylabel("Background rejection (1 - FPR)", size=15)
        plt.xticks(size=15)
        plt.yticks(size=15)
        plt.xlim(0., 1)
        plt.ylim(0., 1)
        plt.legend(loc='lower left', fontsize=15)
        plt.title('One particle vs rest ROC curves', loc='right', size=15)
        plt.grid(b=1)