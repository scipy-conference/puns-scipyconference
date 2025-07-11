"""
Core pun generation functionality for scipyconference.

This module contains the implementation of pun generation functions,
including reading from JSON files and the main create_puns function.
"""

import random
from pathlib import Path

import numpy as np


class objectionable_(str):
    """
    A string subclass. These puns are so bad, type(pun) == np.objectionable_.

    Blame @anzelpwj for the idea.
    """
    pass

objectionable_.__module__ = 'np'  # Making the type properly render as being np
np.objectionable_ = objectionable_

PARTY_EMOJIS = [
    "🎉",
    "🎊",
    "🎈",
    "🎂",
    "🍰",
    "🎁",
    "🎪",
    "🎭",
    "🎨",
    "🎯",
    "🎲",
    "🎮",
    "🎸",
    "🎹",
    "🎺",
    "🎻",
    "🎤",
    "🎧",
    "🎵",
    "🎶",
    "⚡",
    "🦀",
]


def _read_puns_from_json():
    """
    Read puns from the JSONL file.

    Reads the community-curated puns from the puns.json file in JSONL format.
    Each line should contain a JSON object with 'pun' and 'github_username' fields.

    :return: List of dictionaries containing pun data.
        Each dictionary has 'pun' and 'github_username' keys.
        Returns empty list if file is not found or malformed.
    :rtype: list
    """
    pun_path = Path(__file__).parent / "puns.json"
    puns = []
    with open(pun_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                import json

                data = json.loads(line)
                puns.append(data)
    return puns


def create_puns(number: int, return_puns: bool = False) -> list[np.objectionable_] | None:
    """
    Create ``number`` of puns for the SciPy conference.

    This function generates puns for the SciPy conference community. It can work
    in two modes:

    1. Community-curated puns (default): Reads from puns.json file
    3. Party mode: Creates a celebration with random emojis when number is np.inf

    :param int number: Number of puns to generate. Use np.inf for party mode.
    :param bool return_puns: If False, just print puns. Otherwise return them. Default False.

    :return: Either None (if not return_puns) or a list of puns.    

    Examples::

        create_puns(3)  # Generate 3 community-curated puns
        create_puns(np.inf)  # Create a party celebration
        create_puns(3, return_puns=True)  # Gives you a list of puns
    """
    if number is np.inf:
        random_repeats = random.randint(50, 200)
        return_vals = [''] * random_repeats
        for ii in range(random_repeats):
            return_vals[ii] = " ".join(random.sample(PARTY_EMOJIS, random.randint(5, 15)))
        if return_puns:
            return [np.objectionable_(emojis) for emojis in return_vals]
        else:
            print("\n".join(return_vals))
    else:
        puns = _read_puns_from_json()
        if not puns:
            print(
                "No puns found in puns.json. Consider adding some community-curated puns!"  # noqa: E501
            )
            return
        selected_puns = random.choices(puns, k=number)
        if return_puns:
            return [
                np.objectionable_(f"@{pun_data.get('github_username', 'anon')}: {pun_data['pun']}")
                for pun_data in selected_puns]
        else:
            for pun_data in selected_puns:
                print()
                print(f"@{pun_data.get('github_username', 'anon')}: {pun_data['pun']}")
