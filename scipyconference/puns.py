from pathlib import Path
import random

from astropy.table import Table
import numpy as np


def create_puns(number=1):
    """
    The essence of SciPy are puns.

    Parameters
    ----------

    number : int
        Number of puns to generate
    """

    # TODO: no need for astropy
    pun_path = Path(__file__).parent / Path('puns.json')
    all_puns = sorted(Table.read(pun_path, format='pandas.json')['pun'])
    if number is np.inf:
        # TODO: make this to do something really special
        number = len(all_puns)

    selected_puns = random.sample(all_puns, number)

    return selected_puns
