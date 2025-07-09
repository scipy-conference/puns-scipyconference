"""
Core pun generation functionality for scipyconference.

This module contains the implementation of pun generation functions,
including reading from JSON files and the main create_puns function.
"""

import random
from pathlib import Path

import numpy as np


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


def create_puns(number: int):
    """
    Create ``number`` of puns for the SciPy conference.

    This function generates puns for the SciPy conference community. It can work
    in two modes:

    1. Community-curated puns (default): Reads from puns.json file
    3. Party mode: Creates a celebration with random emojis when number is np.inf

    :param int number: Number of puns to generate. Use np.inf for party mode.
    :return: None
    :rtype: None
    :raises ImportError: If llamabot is required but not installed.

    Examples::

        create_puns(3)  # Generate 3 community-curated puns
        create_puns(np.inf)  # Create a party celebration
    """
    if number is np.inf:
        party_emojis = [
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
        random_repeats = random.randint(50, 200)
        for _ in range(random_repeats):
            print(" ".join(random.sample(party_emojis, random.randint(5, 15))))
    else:
        puns = _read_puns_from_json()
        if not puns:
            print(
                "No puns found in puns.json. Consider adding some community-curated puns!"  # noqa: E501
            )
            return
        selected_puns = random.choices(puns, k=number)
        for pun_data in selected_puns:
            print()
            print(f"@{pun_data.get('github_username', 'anon')}: {pun_data['pun']}")