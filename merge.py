import numpy as np
from settings import getSet
import glob

sets = getSet()


def merge(files):
    return np.vstack([np.load(file) for file in files])


def find_all(folder):
    return glob.glob(folder + "/*.npy")


if __name__ == '__main__':
    folder = sets.DEFAULT_TRAIN_FILE_DIRECTORY
    np.save(sets.DEFAULT_TRAIN_FILE_M, merge(find_all(folder)))
